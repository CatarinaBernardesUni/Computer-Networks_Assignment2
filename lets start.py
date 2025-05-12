# The OS module in Python provides functions for interacting with the operating system
import os
# The Platform module is used to retrieve information about the platform on which the program is running
import platform
# The subprocess module is used to run new applications or programs by creating new processes
import subprocess
# The sys module provides functions and variables that are used to manipulate different
# parts of the Python runtime environment
import sys

from datetime import datetime

# print(platform.system()) --- This will print the name of the operating system: Windows

def perform_ping(host):
    """
    Perform a ping operation on the given host.
    """
    # Check if the operating system is Windows
    if platform.system().lower() == 'windows':
        # Use the 'ping' command with '-n' option for Windows
        # The '-4' option is used to force IPv4
        command = ['ping', '-4', '-n', '4', host]
    else:
        # Use the 'ping' command with '-c' option for Linux/Mac
        command = ['ping', '-c', '4', host]

    # Execute the ping command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print the output of the ping command
    print(result.stdout)

perform_ping('google.com')
perform_ping('google.com')