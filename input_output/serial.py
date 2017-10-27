# Purpose: Demonstrate opening a serial port

# Import pyserial
import serial

# Create the serial connection
connection = serial.Serial()
# Set the serial baud rate to 19,200 bps
connection.baudrate = 19200
# Define the connection port
# COM1 Port:
# connection.port = 'COM1'
# Loopback
connection.port = 'loop://'
# Set the timeout to 1 second
connection.timeout = 1
# Open the serial connection
connection.open()
# Check if the connection is open
connection.is_open
# Write information to the serial port
connection.write("Some information")
# Close the serial port
connection.close()
