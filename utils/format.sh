#!/bin/bash

# Formatting, idk if you wanna github-actionify it or something

read -p "Relative directory to format from: " path_from
cd $path_from

echo "NEWLINES:"
utils/add_newlines.sh
