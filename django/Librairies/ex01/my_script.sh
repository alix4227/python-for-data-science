#!/usr/bin/sh
pip --version
pip install git+https://github.com/jaraco/path.git --target=local_lib --upgrade > logs.log
PYTHONPATH=local_lib python3 my_program.py
