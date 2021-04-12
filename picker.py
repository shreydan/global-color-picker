from pynput.mouse import Listener as MouseListener
from pynput.mouse import Button as MouseButton
import pyscreenshot as ImageGrab
from PIL import Image

def getHex(rgb):
    return '%02X%02X%02X'%rgb


def checkColor(xy):
    bbox = (xy[0],xy[1],xy[0]+1,xy[1]+1)
    im = ImageGrab.grab(bbox=bbox)
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    print('rgb value: ',(r,g,b))
    print('hex value: #',getHex((r,g,b)))
    

def onClick(x,y, button, pressed):

    if pressed and button == MouseButton.left:
        checkColor((x,y))

    if pressed and button == MouseButton.right:
        return False



m = MouseListener(on_click=onClick)
m.start()
m.join()
