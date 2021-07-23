from tkinter import *
from PIL import ImageTk, Image
root=Tk()

#image1 = Image.open("images.png")
#image1 = img.resize((50, 50), Image.ANTIALIAS)
#test = ImageTk.PhotoImage(image1)

#label1 = Label(image=test)
#label1.image = test
#label1.place(x=50, y=50)
lbl=Label(root, text="Instructions", fg='red', font=("Helvetica", 20,"bold"))
lbl.place(x=145, y=30)

inst=Label(root, text="1. Click the 'Open Live Detection' button to begin the procedure.", font=("Helvetica",11))
inst.place(x=20, y=90)

qui=Button(root, text="Quit", command=quit)
qui.place(x=205, y=450)

root.title('Instructions')
root.geometry("450x500")
root.mainloop()