from pynput.mouse import Listener as MouseListener
from pynput.mouse import Button as MouseButton
import pyscreenshot as ImageGrab
from PIL import Image

def checkColor(xy):
    im = ImageGrab.grab()
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel(xy)
    print('rgb value: ',(r,g,b))

def onClick(x,y, button, pressed):

    if pressed and button == MouseButton.left:
        checkColor((x,y))

    if pressed and button == MouseButton.right:
        return False



m = MouseListener(on_click=onClick)
m.start()
m.join()