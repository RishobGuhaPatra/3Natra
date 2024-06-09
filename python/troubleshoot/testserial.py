import serial
import time

# Configure the serial connection
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200
)
# serial.write(b'Hello World\n')

def send_command(command):
    ser.write(command.encode())

def clear_display():
    send_command("")

def write_text(text):
    command = text
    send_command(command)

try:
    # Initialize display
    clear_display()
    time.sleep(2)

    # Write text to the display
    write_text("Hello, Rishob! The quick brown fox jumped over the lazy dogs.")
    time.sleep(5)

    # You can write additional lines of text if supported
    write_text("                           Vision Glass")
    time.sleep(10)

finally:
    # Close the serial connection
    ser.close()