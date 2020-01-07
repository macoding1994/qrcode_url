import qrcode
qr = qrcode.QRCode(
	version=2,
	error_correction=qrcode.constants.ERROR_CORRECT_L,
	box_size=10,
	border=1
)#设置二维码的大小
qr.add_data("http://www.tflying.cn/")
qr.make(fit=True)
img = qr.make_image()
img.save("zkfl_blog.png")