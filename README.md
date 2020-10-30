# global-color-picker

`pip install -r requirements.txt`


Click on anywhere on the screen and get the pixel RGB value at the cursor position.

Right-click to stop the program.

Instead of using ImageGrab, this script uses [pyscreenshot](https://pypi.org/project/pyscreenshot/) this is to ensure it works cross-platform since PIL ImageGrab doesn't work on Linux.

