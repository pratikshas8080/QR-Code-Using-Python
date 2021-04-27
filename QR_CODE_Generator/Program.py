import pyqrcode
import png
from pyqrcode import QRCode

s = "www.instagram.com/wecodeinpython/"

url = pyqrcode.create(s)

url.png("myqr.png", scale=6)
