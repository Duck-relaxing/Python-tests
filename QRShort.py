import qrcode
import pyshorteners
import pyshorteners.shorteners
import pyshorteners.shorteners.shortcm

url = input("Información del código QR: ")

short_url = pyshorteners.Shortener().tinyurl.short(url)

print(short_url)

colorqr = input("Color del código QR en ingles: ")
colorfondo = input("Color del fondo del código QR en ingles: ")

qr = qrcode.QRCode(version= 1, box_size=20, border=5)

qr.add_data(short_url)

qr.make(fit=True)
img = qr.make_image(fill_color=colorqr, back_color=colorfondo)
img.save(r"C:\Users\Lenovo\Downloads\python\qr\miqr.png")