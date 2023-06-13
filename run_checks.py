import subprocess
import sys

# Config file
config_file = "commands.config"

# Check type: 1 for quick, 2 for full
check_type = sys.argv[1] if len(sys.argv) > 1 else "2"

# Validate check type
if check_type not in ["1", "2"]:
    print("Invalid check type. Use '1' for quick or '2' for full.")
    sys.exit(1)

# Process each line in the config file
try:
    with open(config_file, "r") as file:
        for line in file:
            # Ignore comments and empty lines
            if line.startswith("#") or line.strip() == "":
                continue

            # Split the line into check_name, command, expected_output, check_type, match_type, keywords
            check_name, command, expected_output, line_check_type, match_type, keywords = map(str.strip, line.split("|"))

            # Check if the check should be executed based on the check type
            if check_type == "1" and line_check_type == "2":
                continue

            # Execute the command and capture the output
            actual_output = subprocess.getoutput(command).strip()

            # Check if match_type is exact
            if match_type == "exact":
                # Compare the actual output with the expected output
                result = "pass" if actual_output == expected_output else "fail"
                # Output the result
                print(f"{check_name}: {result}")
            # Check if match_type is keyword
            elif match_type == "keyword":
                # Check for keywords in the output
                keyword_result = "not found"
                for keyword in keywords.split(","):
                    if keyword in actual_output:
                        keyword_result = "found"
                        break
                # Output the result
                print(f"{check_name}: keywords {keyword_result}")
            else:
                print(f"{check_name}: Invalid match_type specified (use 'exact' or 'keyword')")
except FileNotFoundError:
    print("Error: Config file not found!")
    sys.exit(1)
