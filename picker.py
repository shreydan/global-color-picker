from pynput.mouse import Listener as MouseListener
from pynput.mouse import Button as MouseButton
import pyscreenshot as ImageGrab
from PIL import Image

def checkColor(xy):
    boundingbox = (xy[0],xy[1],xy[0]+1,xy[1]+1)
    im = ImageGrab.grab(bbox=boundingbox)
    rgbim = im.convert('RGB')
    r,g,b = rgbim.getpixel((0,0))
    print('rgb value: ',(r,g,b))
    

def onClick(x,y, button, pressed):

    if pressed and button == MouseButton.left:
        checkColor((x,y))

    if pressed and button == MouseButton.right:
        return False



m = MouseListener(on_click=onClick)
m.start()
m.join()
