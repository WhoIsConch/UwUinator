from codecs import backslashreplace_errors
from tkinter import E
from typing import OrderedDict
from PIL import Image, ImageDraw, ImageFont

img = Image.open("uwuinator/img_copy.jpg")

# Use PIL to write "UwU" in the center of the image
# Make the text very large
# Use the Updock-Regular font

font = ImageFont.truetype("uwuinator-tests/Updock-Regular.ttf", 2000)

ImageDraw.Draw(img).text(((img.width/2)-1500, (img.height/2)-1500), "UwU", fill=(255, 255, 255), font=font)


# ImageDraw.Draw(img).text((img.width / 2 - 10, img.height / 2 - 10), "UwU", fill=(255, 255, 255))

img.save("uwuinator/img_copy_uwu.jpg")

print("Done")