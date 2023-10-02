import PIL
from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename

file_path = askopenfilename()
img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

img = img.resize (myWidth, myHeight), PIL.Image.ANTIALIAS
save_path = asksaveasfilename()
img.save(save_path + "_compressed.jpg")
