import json
import os  # Needed to check the existence of the ping_log file
import platform  # To detect the operating system
import subprocess  # To execute the ping commands
from datetime import datetime  # To make the timestamp of the log entries
from colorama import init, Fore, Style  # To color the output in the terminal

# Initialize colorama
init(autoreset=True)

# Predefined list of hostnames/IPs to be pinged
predefined_list_for_ping = ['google.com', 'yahoo.com', 'bing.com', 'nonexistent.domain.test', '10.255.255.1']

# List to store the results of ping operations
ping_results_log = []

def perform_ping(host):
    """
    Perform a ping operation on the given host and log the result.

    Parameters:
        host (str): The hostname or IP address to ping.

    The function handles platform differences between Windows and Linux systems,
    runs the appropriate ping command, and logs whether the host is reachable with corresponding timestamp.
    """
    # Construct the ping command based on the operating system
    if platform.system().lower() == 'windows':
        # Use the 'ping' command with '-n' option for Windows
        # The '-4' option is used to force IPv4
        command = ['ping', '-4', '-n', '4', host]
    else:
        # Use the 'ping' command with '-c' option for Linux
        command = ['ping', '-4', '-c', '4', host]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{Fore.CYAN}Performing ping on {host} at {timestamp}")

    try:
        # Execute the ping command and capture the output
        # stdout: The standard output of the subprocess, as a bytes object.
        # stderr: The standard error of the subprocess, as a bytes object.
        # 4 is the default timeout of the ping command on Windows
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=4)

        # Check if the ping command was successful
        if result.returncode == 0:
            # Print the output of the ping command
            print(result.stdout)
            print(f"{Fore.GREEN}Host {host} is reachable.")
            status = "reachable"
        else:
            print(f"{Fore.RED}Host {host} is unreachable.\n{result.stderr or result.stdout}")
            status = "unreachable"

    except subprocess.TimeoutExpired:
        # Handle timeout
        print(f"{Fore.RED}Ping to {host} timed out.")
        status = "unreachable"

    except Exception as e:
        # Catch any other exceptions
        print(f"{Fore.RED}An error occurred while pinging {host}: {e}")
        status = "unreachable"

    # Log result
    ping_results_log.append({
        "host": host,
        "status": status,
        "timestamp": timestamp
    })

    print(f"{Fore.CYAN}Finished pinging {host} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 57)


def log_results(results):
    """
    Save the ping results to a file in JSON format under a timestamped key.

    Parameters:
        results (dict): Dictionary with the key being the timestamp of logging and
                        the values a list of results containing host, status, and timestamp.
    """
    log_filename = "ping_log.txt"
    current_timestamp = f"Results from {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    # Load existing data if the file exists and is valid JSON
    if os.path.exists(log_filename):
        try:
            with open(log_filename, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = {}
    else:
        data = {}

    # Add new results under the current timestamp
    data[current_timestamp] = results

    with open(log_filename, "w") as log_file:
        json.dump(data, log_file, indent=5)

def main():
    """
    Main function to use the ping tool.

    - Asks the user whether to use a predefined list or input custom hosts.
    - Performs ping on each host.
    - Displays a summary of results.
    - Saves the results to a file.
    """
    print(f"{Style.BRIGHT}Starting the ping tool...\n")
    choice = input("Do you want to ping a predefined list of hosts? (y/n):\t").strip().lower()

    if choice == 'y':
        hosts = predefined_list_for_ping
    else:
        user_input = input("Enter the hostnames or IP addresses to ping separated by commas:\t")
        # Split user input into a list and remove any extra spaces
        hosts = [host.strip() for host in user_input.split(',') if host.strip()]

    if not hosts:
        print("No valid hosts provided. Exiting.")
        return

    # Perform ping for each host
    for h in hosts:
        perform_ping(h)

    # Notify user that all pings are completed
    print("All ping operations completed.")

    # Print summary
    print(f"\n{Style.BRIGHT}Ping Summary:")
    for log in ping_results_log:
        color = Fore.GREEN if log['status'] == 'reachable' else Fore.RED
        print(f"{color}{log['host']} - {log['status']} at {Fore.BLUE}{log['timestamp']}")

    # Write results to a file
    log_results(ping_results_log)


if __name__ == "__main__":
    main()