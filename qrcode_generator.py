#pip install pyqrcode
import pyqrcode
from PIL import Image
link = input("Enter anything to generate the QR Code: ")
qr_code = pyqrcode.create(link)
qr_code.png('qrcode.png', scale=5)
Image.open('qrcode.png')