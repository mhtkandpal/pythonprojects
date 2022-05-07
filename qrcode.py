import qrcode as qr

img=qr.make("https://demo.silamoney.com/")
img.save("sila.png")
