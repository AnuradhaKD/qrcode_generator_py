import pyqrcode
from pyqrcode import QRCode

get_link = input("Enter your URL : ")

url = pyqrcode.create(get_link)

url.svg(qr_code.svg, scale = 8)