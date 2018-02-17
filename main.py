#!/usr/bin/env python
#coding:UTF-8

# Please install Pillow by pip
import sys
import qrcode
from datetime import datetime

argvs = sys.argv
starttime = datetime.now().strftime('%H%M%S')

directory = './images/'

if argvs[1] == '-h' or argvs[1] == '--help':
    print ''
    print 'Usage: ./main.py [strings]'
    print 'QRcode saves for images directory'
    print ''

else:
    img = qrcode.make(argvs[1])
    img.save(directory + starttime + '.png')