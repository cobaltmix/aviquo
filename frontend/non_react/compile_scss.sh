#!/bin/bash

find . -type f -name '*.scss' | while read -r scss_file; do
  css_file="${scss_file%.scss}.css"
  echo "Compiling $scss_file to $css_file"
  sass "$scss_file" "$css_file"
done
