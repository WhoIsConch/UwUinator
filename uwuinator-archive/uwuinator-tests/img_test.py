
with open("uwuinator/img.jpg", "rb") as f:
    data = f.read()

    with open("uwuinator/img_copy.jpg", "wb") as f:
        f.write(data)

print("Done")