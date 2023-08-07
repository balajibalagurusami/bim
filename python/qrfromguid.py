import qrcode

# Open the file containing GUIDs
with open("guid.txt", "r") as f:
    guids = [line.strip() for line in f.readlines()]

# Prefix and suffix for each GUID to create a URL
prefix = "https://speckle.xyz/streams/1382210fe3/commits/9194161bc9?c=%5B-12.92497,-21.468,20.69264,2.36178,-3.4837,2.8535,0,1%5D&filter=%7B%22isolatedIds%22%3A%5B%22"
suffix = "%22%5D%7D"

# Generate URLs for each GUID and save as QR codes
for guid in guids:
    url = prefix + guid + suffix
    img = qrcode.make(url)
    img.save(f"{guid}.png")

