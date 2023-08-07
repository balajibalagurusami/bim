pip install qrcode
pip install png
pip install pypng
import qrcode
import png
import os

# Specify the path to the input file and output folder
input_file = "text_file.txt"
output_folder = "qr_codes/"

# Create the output folder if it doesn't already exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Read the input file and generate a QR code for each line
with open(input_file, "r") as f:
    for line in f:
        # Remove any leading/trailing whitespace and newlines
        line = line.strip()
        
        # Generate the QR code
        qr = qrcode.QRCode(version=None, box_size=10, border=4)
        qr.add_data(line)
        qr.make(fit=True)
        qr_data = qr.get_matrix()
        
        # Convert the QR code data to a PNG image
        png_image = png.from_array(qr_data, "L")
        
        # Save the PNG image with the same name as the text value
        with open(output_folder + line + ".png", "wb") as outfile:
            png_image.save(outfile)
