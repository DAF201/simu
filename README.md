# simu
modbus simulator with GUI (Made with HTML, the only GUI took I know how to use)

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

> or make a bat file if you don't like console but stil need a HTML UI (@SomeTesters in your company who don't know computer. Yes, there are quite a lot of them in where I am currently working.):
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

