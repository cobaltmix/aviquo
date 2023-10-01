#!/bin/bash

find . -type f \( -name "*.md" -o -name "*.html" -o -name "*.py" -o -name "*.css" -o -name "*.js" \) -not -path "*/node_modules/*" | while IFS= read -r file; do
    echo -n -e "\033[1K"
    echo -n -e "\r$file"
    sed -i -e :a -e '/^\n*$/{$d;N;ba' -e '}' "$file"
    # echo "" >> "$file"
done

echo