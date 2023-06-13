# Server Health Check Tool

This tool is designed to automate the process of running health checks on servers to ensure that specific processes are running as expected. It allows for both quick and full health checks, with options to look for an exact match or search for keywords in the command responses.

# Features
Configure custom shell commands to check server health.
Specify expected outputs for exact matches.
Specify keywords to look for in the command output.
Differentiate between quick checks and full checks.
Configurable through an XML file.
User-friendly output indicating pass or fail status for each check.

# Usage
# Configuration File
The tool uses an XML configuration file (commands.config.xml) that specifies the checks to be run. The structure of the configuration file is as follows:
