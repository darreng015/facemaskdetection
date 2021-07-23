from tkinter import *
from tkinter import ttk
import os
import cv2

window=Tk()

bg = PhotoImage(file = "images.png")

def detect ():
    os.system("python detect_mask.py")
def graph ():
    plotgraph=cv2.imread("output/plot.png")
    cv2.imshow("Training Graph", plotgraph)
def instructions ():
    os.system("python instructions_detect.py")

canvas1 = Canvas( window, width = 400, height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg, anchor = "nw")

canvas1.create_text(250,50, text="Face Mask Detection", font=("Orator Std", 30))
#lbl.place(x=130, y=50)

live=Button(window, text="Open Live Detection", command=detect,fg='blue')
live.place(x=200, y=100)

inst=Button(window, text="Instructions", command=instructions, fg='blue')
inst.place(x=220, y=135)

train=Button(window, text="Train Model with Dataset", command=graph, fg='red')
train.place(x=187, y=200)

inst=Button(window, text="Instructions", fg='red')
inst.place(x=220, y=235)




window.title('Face Mask Detection')
window.geometry("500x350")
window.mainloop()