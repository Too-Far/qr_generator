'''QR codes are simply data turned into strings for machines to read.
This program creates a QR code for a home wifi (to be able to give to guests, etc). You can make nearly anything with this program. IE, QR codes for your social media, websites, serial numbers, etc. 
'''

import pyqrcode as pq

ssid = 'MySpectrumWiFi65-5g' #Put whatever the network name is here
security = 'WEP' #Put whether the security is WPA or WEP
password = 'desertmarble318' #WIFI password here
#Creates QR code 
#qr = pq.create(f'WIFI:S:{ssid}; T: {security} ;P: {password};;')
qr = pq.create(f'WIFI:S:{ssid};;')
#Turns QR code into PNG for printing
with open('WIFI.png', 'w') as fstream:
    qr.png('WIFI.png', scale=5)

#Can also create an SVG file:
# qr.svg('WIFI.svg', scale=4)

#Or simply print to terminal:
print(qr.terminal())

#coment comment comment
