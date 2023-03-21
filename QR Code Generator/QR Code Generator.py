from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
root = Tk()

def generate():
    link_name = linkname_entry.get()
    link = link_entry.get()
    filename = link_name+ '.png'
    url = pyqrcode.create(link)
    url.png(filename, scale=8)
    image = ImageTk.PhotoImage(Image.open(filename))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 450, window=image_label)

canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = Label(root, text='QR Code Generator', fg='grey', font=('Arial',30))
link_name_label = Label(root, text='Link Name:')
link_label = Label(root, text='Label:')
linkname_entry = Entry(root)
link_entry = Entry(root)
button = Button(root, text='generate QR code', command=generate)

canvas.create_window(200,50, window=app_label)
canvas.create_window(200,100, window=link_name_label)
canvas.create_window(200,130, window=linkname_entry)
canvas.create_window(200,160, window=link_label)
canvas.create_window(200, 180, window=link_entry)
canvas.create_window(200, 220, window=button)
root.mainloop()