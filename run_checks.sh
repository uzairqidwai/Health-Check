#!/bin/bash

# Config file
CONFIG_FILE="commands.config"

# Check type: 1 for quick, 2 for full
CHECK_TYPE="${1:-2}"

# Check if the config file exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Config file not found!"
    exit 1
fi

# Validate check type
if [ "$CHECK_TYPE" != "1" ] && [ "$CHECK_TYPE" != "2" ]; then
    echo "Invalid check type. Use '1' for quick or '2' for full."
    exit 1
fi

# Loop through each line in the config file
while IFS= read -r line || [ -n "$line" ]; do
    # Ignore comments and empty lines
    if [[ $line == \#* ]] || [[ -z $line ]]; then
        continue
    fi
    
    # Split the line into check_name, command, expected_output, check_type
    IFS='|' read -r -a array <<< "$line"
    check_name=${array[0]}
    command=${array[1]}
    expected_output=${array[2]}
    check_type=${array[3]}
    
    # Check if the check should be executed based on the check type
    if [ "$CHECK_TYPE" == "1" ] && [ "$check_type" == "2" ]; then
        continue
    fi
    
    # Execute the command and capture the output
    actual_output=$(eval $command)
    
    # Compare the actual output with the expected output
    if [ "$actual_output" == "$expected_output" ]; then
        echo "$check_name: pass"
    else
        echo "$check_name: fail"
    fi
done < "$CONFIG_FILE"