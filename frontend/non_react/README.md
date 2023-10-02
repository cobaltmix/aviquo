# Dev Here

Basically stuff that was not here before is here now

To compile scss, install a **SASS** (not **scss**) compiler and compile scss BEFORE running things

Download compiler here or use your package manager:
<https://github.com/sass/dart-sass/releases/tag/1.68.0>

Then run compile_scss.sh (The sass compiler should be called sass for this to work, make an alias if it isn't)
auto_compile_scss.sh is for dev, it automatically recompiles scss on change to scss

To host these:

./run_dev_server.sh
in the directory where you want to test stuff, copy if missing.

and go to localhost:8080

For mobile device testing, use the inspect element window and resize it. (most phones are 300px-500px viewport wide)
