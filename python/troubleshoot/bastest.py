import subprocess
import os, sys

sudo_password = "orangepi"

# Path to the virtual environment's Python executable
venv_python_path = "/home/orangepi/googlenv/bin/python3"

# Path to the script to be called
script_to_run = "home/orangepi/googlenv/Testlanguagetranslation.py"

# Arguments to pass to the script (optional)
args = ["arg1", "arg2"]

# Combine the Python executable, script path, and arguments
command = [venv_python_path, script_to_run]

# Run the command
#subprocess.run(command)
subprocess.call(['python3', venv_python_path, script_to_run])