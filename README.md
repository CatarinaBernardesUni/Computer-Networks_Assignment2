# Network Ping Diagnostic Tool

A Python-based network diagnostic tool that performs ping operations on specified hosts and logs the results with timestamps.

## Features

- **Interactive Mode**: Choose between a predefined list of hosts or enter custom hostnames/IP addresses
- **Cross-Platform Support**: Works on both Windows and Linux systems
- **Predefined Host List**: Includes common domains (google.com, yahoo.com, bing.com) for quick testing
- **Comprehensive Logging**: Stores ping results in JSON format with timestamps in `ping_log.txt`
- **Color-Coded Output**: Uses colorama for easy-to-read terminal output
- **Error Handling**: Handles unreachable hosts, timeouts, and connection errors
- **Result Summary**: Displays a summary of all ping operations after completion

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/CatarinaBernardesUni/Computer-Networks_Assignment2.git
   cd Computer-Networks_Assignment2
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```bash
python ping_tool.py
```

The tool will prompt you to:
1. Choose between using a predefined list or entering custom hosts
2. If custom: Enter hostnames or IP addresses separated by commas

The results will be displayed in the terminal and logged to `ping_log.txt`.

## Output

The tool provides:
- Real-time ping results with color-coded status indicators
- A summary of all ping operations
- JSON-formatted log file with timestamps for each ping session

## Note

Created as part of the second assignment for Computer Networks and Cloud Computing (Spring Semester, 2025).
