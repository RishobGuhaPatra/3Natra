import subprocess

# Path to the Python executable in Virtual Environment B
venv_b_python = "/home/orangepi/googlenv/bin/python"

# Path to Program B
program_b_path = "/home/orangepi/googlenv/ProgramInvenv.py"


#result = subprocess.run(['python', 'program_b_path', 'Please Translate in Marathi'], capture_output=True, text=True)

# Print the output of script2.py
#print("Output from script2.py:", result.stdout.decode())

# Run Program B and capture the output
result = subprocess.run(
    [venv_b_python, program_b_path, 'Please Translate in Marathi'], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE
)

# Display the output
print("Program B Output:")
print(result.stdout.decode())

#if result.returncode != 0:
#    print("Error:", result.stderr.decode())
