#!/bin/bash

while true; do
    find ./ -name "*.scss" | inotifywait -e modify -e create -e delete -e move -q -r ./ >/dev/null && {
        ./compile_scss.sh
        echo "Recompiled"
    }
    sleep 0.2
done

