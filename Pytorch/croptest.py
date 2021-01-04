from PIL import Image

im = Image.open('13708.jpg')
im = im.crop((220.56845, 382.88434, 468.46558, 962.74396))
im.save('_0.jpg')
