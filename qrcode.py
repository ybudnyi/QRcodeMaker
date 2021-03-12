import qrcode
import pyperclip
import os
import sys
'''This program allows you to make QRcodes from site which url is copy in your clipboard.
    - Copy URL of site in your clipboard (Ctrl + C)
    - Run this program'''

from_buff = str(pyperclip.paste())
print(from_buff)
#name_of_site = sys.argv[1]
name_of_site = input('Input name for your QRcode --- ')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


if not os.path.exists('D:\\Documents\\QRcodes'):
    os.mkdir('D:\\Documents\\QRcodes')

os.chdir('D:\\Documents\\QRcodes')
qr.add_data(from_buff)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(name_of_site + '.jpg')
print(f'Your image is save in {os.getcwd()}')

input('Press Enter for Exit...')