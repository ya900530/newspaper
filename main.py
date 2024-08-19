import os

import files
import img2pdf
import PyPDF2
from PIL import Image
from PIL import Image

# Open an image file
def resize01( inputnum):
    img01 = Image.open('input%d.jpg' %inputnum)
    img02 = Image.open('main.jpg')
    A4_WIDTH = 2480
    A4_HEIGHT = 3508
    # Create a new blank image with white background
    canvas = Image.new('RGB', (A4_WIDTH, A4_HEIGHT), 'white')
    width, height = img01.size
    new_width = 1090
    new_height = int(height * new_width / width)
    resized_img01 = img01.resize((new_width, new_height))
    result = Image.new("L", (2480, 3508))
    result.paste(img02, (0, 0))
    result.paste(resized_img01, (530, 680))
    result.save("print%d.jpg" %inputnum)
    # Save the blank canvas
    # canvas.save('blank_A4_canvas.jpg')
    # Save the resized image
    # resized_img01.save('%d.jpg' %inputnum)
resize01(1)
resize01(2)
resize01(3)
resize01(4)
resize01(5)
resize01(6)
resize01(7)
resize01(8)
resize01(9)
# resize01(10)
# resize01(11)
# resize01(12)
# resize01(13)
# resize01(14)
# resize01(15)
# resize01(16)
# resize01(17)
# resize01(18)
# resize01(19)
# resize01(20)
# resize01(21)
# resize01(22)
# resize01(23)
# resize01(24)
# resize01(25)
# os.rename('imgs','images')
# os.chdir("images")
#
# imgs = os.listdir()
# imgs.sort()
# for ind,img in enumerate(imgs):
#     #open each image
#     with Image.open(img) as Image:
#         # convert the image to a PDF
#         pdf = img2pdf.convert(image.filename)
#         # write the PDF to its final destination
#         with open(f"../pdfs/pdf{ind + 1}.pdf", "wb") as file:
#             file.write(pdf)
#             print(f"Converted {img} to pdf{ind + 1}.pdf")
# os.chdir("pdfs")
# pdfs = os.listdir()
# pdfMerge = PyPDF2.PdfMerger()
#
# # loop through each pdf page
# for pdf in pdfs:
#   # open each pdf
#   with open(pdf, 'rb') as pdfFile:
#     # merge each file
#     pdfMerge.append(PyPDF2.PdfReader(pdfFile))
#
# # write the merged pdf
# pdfMerge.write('merged.pdf')
#
# # download the final pdf
# files.download('merged.pdf')

# Resize the image
# A4_WIDTH = 2480
# A4_HEIGHT = 3508
#
# # Create a new blank image with white background
# canvas = Image.new('RGB', (A4_WIDTH, A4_HEIGHT), 'white')
#
#
# width, height = img01.size
# new_width = 1090
# new_height = int(height * new_width / width)
# resized_img01 = img01.resize((new_width, new_height))
#
# result = Image.new("RGB", (2480, 3508))
# result.paste(canvas, (0, 0))
# result.paste(resized_img01, (509, 665))
# result.save("result.jpg")
# # Save the blank canvas
# canvas.save('blank_A4_canvas.jpg')
# # Save the resized image
# resized_img01.save('output.jpg')
