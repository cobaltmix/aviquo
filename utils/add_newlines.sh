#/bin/bash

find ../auth -type f -exec sh -c 'if [ "$(tail -c 1 "$0" 2>/dev/null)" != "\n" ]; then echo "" >> "$0"; fi' {} \;
