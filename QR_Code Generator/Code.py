#importing qrcode
import qrcode

url = input("Enter the url:")
img = qrcode.make(url)
#saving the image
img.save("QR_code.png")
