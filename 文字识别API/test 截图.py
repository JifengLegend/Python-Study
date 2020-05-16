from PIL import ImageGrab
im = ImageGrab.grabclipboard()
im.save('cache.png','PNG')