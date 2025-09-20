import qrcode

# Your site link
url = "https://jest-bay.vercel.app/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)

# Save as image
img = qr.make_image(fill_color="black", back_color="white")
img.save("jestbay_qr.png")
