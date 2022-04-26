from PIL import Image, ImageDraw, ImageFont

# img = Image.open("uwuinator/img_copy.jpg")

# Use PIL to write "UwU" in the center of the image
# Make the text very large
# Use the Updock-Regular font

def generate_gradient(
        colour1: str, colour2: str, width: int = 10000, height: int = 10000) -> Image:
    """Generate a vertical gradient."""
    base = Image.new('RGB', (width, height), colour1)
    top = Image.new('RGB', (width, height), colour2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

generate_gradient("blue", "cyan").save("uwuinator/img_copy_uwu_3.jpg")

print("DOne")