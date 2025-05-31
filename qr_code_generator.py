import qrcode

# Data to be encoded
data ="https://youtu.be/PMzTLWTWLZU?si=1T3tthmmF5nIMdfr"

qr=qrcode.QRCode(version=4,
                 box_size=7,
                 border=7)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color = 'blue',
                    back_color = 'white')

img.save('MyQRCode2.png')
img.show()