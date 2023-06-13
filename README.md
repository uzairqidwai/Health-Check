# Server Health Check Tool

This tool is designed to automate the process of running health checks on servers to ensure that specific processes are running as expected. It allows for both quick and full health checks, with options to look for an exact match or search for keywords in the command responses.

## Features

- Configure custom shell commands to check server health.
- Specify expected outputs for exact matches.
- Specify keywords to look for in the command output.
- Differentiate between quick checks and full checks.
- Configurable through an XML file.
- User-friendly output indicating pass or fail status for each check.

## Usage

### Configuration File

The tool uses an XML configuration file (`commands.config.xml`) that specifies the checks to be run. The structure of the configuration file is as follows:

```xml
<checks>
    <check>
        <name>Name of the check</name>
        <command>Shell command to run</command>
        <expectedOutput>Expected output for exact match</expectedOutput>
        <checkType>1 for quick, 2 for full check</checkType>
        <matchType>exact or keyword</matchType>
        <keywords>Comma-separated keywords for keyword search</keywords>
    </check>
    <!-- Add more checks as needed -->
</checks>
```

## Running the Tool

Execute the script with Python:

```shell
python run_checks.py [check_type]
```
Replace [check_type] with 1 for a quick check or 2 for a full check. If not specified, it defaults to a full check.

## Requirements
Python 3.x
