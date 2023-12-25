[![rm1](https://img.shields.io/badge/rM1-supported-green)](https://remarkable.com/store/remarkable) [![rm2](https://img.shields.io/badge/rM2-supported-green)](https://remarkable.com/store/remarkable-2) [![Discord](https://img.shields.io/discord/385916768696139794.svg?label=reMarkable&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/ATqQGfu)

reMarkable Template Python Carta Application
============================================

- [.github/workflows/build.yml](.github/workflows/build.yml) - Workflow to build, package, and test the app
- [myapp/\_\_init\_\_.py](myapp/__init__.py) - Main import of the application. The main method gets run on startup.
- [myapp/\_\_main\_\_.py](myapp/__main__.py) - Main entrypoint of the application when used as a python module.
- [myapp.py](myapp.py) - Main entrypoint of the application when compiled with [nuitka](https://nuitka.net/) to create the binary executable.
- [myapp.oxide](myapp.oxide) - [Oxide application registration](https://oxide.eeems.codes/documentation/03_application_registration_format.html).
- [package](package) - [Toltec package recipe](https://github.com/toltec-dev/toltec/blob/stable/docs/package.md) to create a package that can be installed on the device.

Testing
=======

Simulate
========

You can use [rmkit-sim](https://pypi.org/project/rmkit-sim/) to test your application on your local machine.
```bash
make simulate
```

On Device
=========

First you will need to install the following dependencies on the device:
```bash
opkg update
opkg install python3 python3-pip
pip install carta
```

You can now copy the contents of this folder to your device, and run your app with the following from the folder with the code:
```bash
pip install -r ./requirements.txt
python -m myapp
```
