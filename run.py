#!/usr/bin/env python3

# This script sets up a Python virtual environment, installs necessary packages, and runs the download script
import subprocess
import sys
import os

pip_executable = os.path.join('myenv', 'bin', 'pip')
python_executable = os.path.join('myenv', 'bin', 'python')

subprocess.run([sys.executable, '-m', 'venv', 'myenv'])
subprocess.run(['source', './myenv/bin/activate'], shell=True)
subprocess.run([pip_executable, 'install', 'selenium', 'requests'])
subprocess.run([python_executable, './download.py'])
subprocess.run(['deactivate'], shell=True)