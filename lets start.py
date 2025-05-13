import json
# The Platform module is used to retrieve information about the platform on which the program is running
import platform
# The subprocess module is used to run new applications or programs by creating new processes
import subprocess
# The sys module provides functions and variables that are used to manipulate different
# parts of the Python runtime environment
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

predefined_list_for_ping = ['google.com', 'yahoo.com', 'bing.com', 'nonexistent.domain.test', '10.255.255.1']

# To store logs
ping_results_log = []


def perform_ping(host):
    """
    Perform a ping operation on the given host.
    :param host: Hostname or IP address to ping.
    """
    # Check if the operating system is Windows
    if platform.system().lower() == 'windows':
        # Use the 'ping' command with '-n' option for Windows
        # The '-4' option is used to force IPv4
        command = ['ping', '-4', '-n', '4', host]
    else:
        # Use the 'ping' command with '-c' option for Linux
        command = ['ping', '-4', '-c', '4', host]

    # print(f"Performing ping on {host} at {datetime.now()}")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{Fore.CYAN}Performing ping on {host} at {timestamp}")

    try:
        # Execute the ping command and capture the output
        # stdout: The standard output of the subprocess, as a bytes object.
        # stderr: The standard error of the subprocess, as a bytes object.
        # 4 is the default timeout of the ping command on windows
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=4)

        if result.returncode == 0:
            print(f"{Fore.GREEN}Host {host} is reachable.")
            # Print the output of the ping command
            print(result.stdout)
            status = "reachable"
        else:
            # print(f"Failed to reach {host}.\nError:\n{result.stderr or result.stdout}")
            print(f"{Fore.RED}Host {host} is unreachable.\n{result.stderr or result.stdout}")
            status = "unreachable"

    except subprocess.TimeoutExpired:
        # print(f"Ping to {host} timed out.")
        print(f"{Fore.RED}Ping to {host} timed out.")
        status = "unreachable"

    except Exception as e:
        # print(f"An error occurred while pinging {host}: {e}")
        print(f"{Fore.RED}An error occurred while pinging {host}: {e}")
        status = "unreachable"

    # Log result
    ping_results_log.append({
        "host": host,
        "status": status,
        "timestamp": timestamp
    })

    # print(f"Finished pinging {host} at {datetime.now()}")
    print(f"{Fore.CYAN}Finished pinging {host} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 57)


def log_results(results):
    with open("ping_log.txt", "w") as log_file:
        json.dump(results, log_file, indent=5)


def main():
    # print("Starting the ping tool...\n")
    print(f"{Style.BRIGHT}Starting the ping tool...\n")
    choice = input("Do you want to ping a predefined list of hosts? (y/n):\t").strip().lower()

    if choice == 'y':
        hosts = predefined_list_for_ping
    else:
        user_input = input("Enter the hostnames or IP addresses to ping separated by commas:\t")
        hosts = [host.strip() for host in user_input.split(',') if host.strip()]

    if not hosts:
        print("No valid hosts provided. Exiting.")
        return

    for h in hosts:
        perform_ping(h)
    print("All ping operations completed.")

    # Print summary
    print(f"\n{Style.BRIGHT}Ping Summary:")
    for log in ping_results_log:
        color = Fore.GREEN if log['status'] == 'reachable' else Fore.RED
        print(f"{color}{log['host']} - {log['status']} at {Fore.BLUE}{log['timestamp']}")
    log_results(ping_results_log)


if __name__ == "__main__":
    # Check if the script is being run directly
    # If so, call the main function
    main()
