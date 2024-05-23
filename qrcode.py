import qrcode 
qr=qrcode.QRCode(
version=15,
box_size=10,
border=5     
)
data= "https://internshala.com/chat/c-74388580?filter=all"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save('text.png')
