#!/bin/bash

# Display Figlet message
echo "nermus" | figlet -f larry3d


# Suggested commands with hierarchy
commands=$(cat <<EOF
Suggested Commands
- fastfetch: System & OS info
- btop: Monitor system processes
EOF
)

# Use 'boxes' with the 'ansi-rounded' theme
echo -e "$commands" | boxes -d ansi-double