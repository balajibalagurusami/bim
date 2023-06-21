import qrcode
# Open the file containing URLs
with open("urls.txt", "r") as f:
    urls = [line.strip() for line in f.readlines()]
# Generate QR codes for each URL and save as PNG files
for i, url in enumerate(urls):
    img = qrcode.make(url)
    img.save(f"qrcode_{i}.png")