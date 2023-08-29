from PIL import Image, ImageDraw, ImageFont


def spongebob(meme):
    result = ""
    for i, letters in enumerate(meme):
        if i % 2 != 0:
            result += letters.lower()
        else:
            result += letters.upper()
    return result


meme = input("Input serious quote here:   ")

font = ImageFont.truetype("comicbd.ttf", 50)

img = Image.open("spongebob.png")

draw = ImageDraw.Draw(img)
text = spongebob(meme)

text_box = draw.textbbox((0, 0), text, font=font)
text_width = text_box[2] - text_box[0]
y_pos = 0

x_pos = (img.width - text_width) / 2

# draw the text on the image
draw.text((x_pos, y_pos), text, (1, 1, 1), font=font)
img.show()
