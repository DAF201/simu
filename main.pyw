from flask import Flask, render_template, request
import threading
from json import load, loads, dump
import webbrowser
from gc import collect
from modbus.modbus import *
import argparse
import os

app = Flask(__name__, static_folder='./static',
            template_folder='./templates')

REGISTERS_DATA = {}
with open('db.json')as db:
    REGISTERS_DATA = load(db)


def db_update():
    with open('db.json', 'w')as db:
        dump(REGISTERS_DATA, db)
    collect()


def str_slice(string):
    res = []
    for x in range(0, len(string), 2):
        if x < len(string)-1:
            res.append(string[x]+string[x+1])
        else:
            res.append(string[x])
    return res


def odd_even_switch(list):
    for x in range(0, len(list), 2):
        if x < len(list)-1:
            temp = list[x]
            list[x] = list[x+1]
            list[x+1] = temp
        else:
            pass


def list_merge(list, reverse=False):
    res = []
    for x in range(0, len(list), 2):
        if x < len(list)-1:
            res.append(list[x]+list[x+1])
        else:
            if reverse:
                res.append('00'+list[x])
            else:
                res.append(list[x]+'00')
    return res


def string_to_ascii(string):
    res = list(string)
    for x in range(0, len(res)):
        res[x] = hex(ord(res[x]))[2:]
    return res


@app.route('/')
def control_panel():
    collect()
    return render_template('home.html')


@app.route('/get_register_data')
def get_register_data():
    return str(REGISTERS_DATA)[1:-1]


@app.route('/update_data', methods=['post'])
def update_register_data():

    post_param = loads(request.get_data().decode())

    register_start = min(int(post_param['register_start']), int(
        post_param['register_end']))
    register_end = max(int(post_param['register_start']), int(
        post_param['register_end']))+1
    register_value = int(post_param['register_value'], 16)

    if register_value > 65535:
        register_value = 'ffff'
    else:
        register_value = hex(register_value)[2:].rjust(4, '0')

    for x in range(register_start, register_end):
        REGISTERS_DATA[str(x)] = register_value

    db_update()

    return str(REGISTERS_DATA)[1:-1]


@app.route('/write_string', methods=['post'])
def write_string():
    post_param = loads(request.get_data().decode())

    start_register = post_param['register_start']
    if int(start_register) > 45000 or int(start_register) < 40000:
        return '', 200

    str_data = string_to_ascii(post_param['register_value'])
    odd_even_switch(str_data)
    str_data = list_merge(str_data, reverse=True)

    for x in range(len(str_data)):
        REGISTERS_DATA[str(int(start_register)+x)] = str_data[x]

    db_update()

    return '', 200


@app.route('/fault_test', methods=['post'])
def check_box():
    fault_data = loads(request.get_data().decode())
    register = fault_data['register']
    data = ''

    for x in range(1, 17):
        data = data+str(int(fault_data[str(x)]))
    REGISTERS_DATA[register] = hex(int(data, 2))[2:]

    db_update()

    return '', 200


@app.route('/exit', methods=['post'])
def exit_simu():
    try:
        return '', 200
    except Exception as e:
        print(e)
    finally:
        os._exit(1)


def open_new_tab():
    webbrowser.open("http://127.0.0.1:80")


def main(args):
    try:
        simulator = threading.Thread(
            target=run, args=[args.visual, args.update, args.serial, args.timeout, args.baudrate, args.xonxoff, args.rtscts, args.dsrdtr])
        server = threading.Thread(target=app.run, args=('0.0.0.0', 80))
        server.daemon = True
        broswer = threading.Thread(target=open_new_tab)
        simulator.start()
        server.start()
        broswer.start()
    except Exception as e:
        print(e)
        os._exit(-1)


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-s', '--serial', type=str,
                           default=AVAILABLE_SERIAL_PORTS[0])
    argparser.add_argument('-t', '--timeout', type=float, default=0.15)
    argparser.add_argument('-b', '--baudrate', type=int, default=115200)
    argparser.add_argument('-x', '--xonxoff', type=int, default=0)
    argparser.add_argument('-r', '--rtscts', type=int, default=0)
    argparser.add_argument('-d', '--dsrdtr', type=int, default=0)
    argparser.add_argument('-u', '--update', type=int, default=1)
    argparser.add_argument('-v', '--visual', action='store_true')
    args = argparser.parse_args()
    main(args)
