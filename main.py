import tkinter
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.minsize(1000, 1000)
window.title("HAPPY BIRTHDAY SADIE!!!")
# Create a photoimage object of the image in the path
label = Label(text="Happy Birthday, Sadie! I love you SO much!", font=("Haettenschweiler", 24))
label.place(x=250, y=100)
other_label = Label(text="Love,Sacha", font=("SimSun", 20))
other_label.place(x=285, y=130)
image1 = Image.open("birthday-cake-sbv.gif")
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=250, y=250)

window.mainloop()