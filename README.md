# simu
modbus simulator with GUI (Made with HTML, the only GUI took I know how to use. Also you many want to change the db.json if your registers don't start from 40000)

Requirements:

```python
(install_requires=['pyserial>=3.5','Flask>=2.2.2'], python_requires=">=3.9")
```

packages shortcut:

```shell
pip install flask & pip install pyserial
```

Usage:

> download, unzip to somewhere, cd to the simu folder
> ```shell
> python main.pyw [-s --serial default: first COM available]
> [-t --timeout default:0.15] 
> [-b --baudrate default:115200]
> [-x --xonxoff default: 0]
> [-r --rtscts default: 0]
> [-d --dsrdtr default: 0]
> [-v --visual default: 0]
> ```

> or make a bat file if you don't like console but stil need a HTML UI (@SomeTesters in your company who don't know computer.):
> ```bat
> start pythonw main.pyw [-s --serial default: first COM available]
> [-t --timeout default:0.15] 
> [-b --baudrate default:115200]
> [-x --xonxoff default: 0]
> [-r --rtscts default: 0]
> [-d --dsrdtr default: 0]
> ```
No GUI and oneline ready to use version see this: [virtual_simulator](https://github.com/DAF201/virtual_simulator)

(github really should count js in HTML also rather than count whole thing as html)

# for testers who don't know computer:

## ask company's programming guy to help with installing Python, pip and required packages first before use

Extract the zip file, go to the simu folder. Right click on simu.bat(no console) or simuv.bat(with console), send to desktop. 

> ask the programming guy to help with add config such as baudrate things in bat file if needed

<img src='https://github.com/DAF201/simu/blob/main/images/Screenshot%20(142).png'>

Double click on the shortcut on desktop, done (the browser will pop out automatically after a short period, if not, try enter https://127.0.0.1:80)

<img src='https://github.com/DAF201/simu/blob/main/images/Screenshot%20(145).png'>

To close the program, just unplug the serial port tool from your PC's USB port or go to the GUI click on exit testing button on the bottom of the page

# GUI guide book

<img src='https://github.com/DAF201/simu/blob/main/images/Screenshot%20(146).png'>

<img src='https://github.com/DAF201/simu/blob/main/images/Screenshot%20(144).png'>

<img src='https://github.com/DAF201/simu/blob/main/images/B9E3300F-D894-4E76-B257-D8949BBBC91D.jpg'>

<img src='https://github.com/DAF201/simu/blob/main/images/Screenshot%20(147).png'>

<img src='https://github.com/DAF201/simu/blob/main/images/61E45682-4AF9-4503-B197-2DED6C8FD722.jpg'>

I am not very familiar with the faults registers of this board so no faults test example...
