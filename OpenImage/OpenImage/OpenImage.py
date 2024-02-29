# open method used to open different extension image file
#im = Image.open(r"C:\Users\user\source\repos\ImageManipulation\ImageManipulation\woman.png") 
  
# This method will show image in any image viewer 
#im.show() 

#img = plt.imread('moon.png') #reads image data
#plt.hist(img.ravel(), 256,[0, 256]) #calculating histogram
#plt.show()



import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import imghdr


window = Tk() #instantiate an instance of a window
window.geometry("500x500") #set the size of a window
window.title("Image Opener") #set the title of a window

def click():
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

    type = imghdr.what(filename, h=None)

    if type=='gif':
         photo = PhotoImage(file = filename)
         label = Label(window,bg="#C8A2C8",fg="black",relief="raised",bd=10,image=photo,compound="bottom") #creates a label and customize it
         label.pack()
    else:
         img = cv.imread(filename,0)
         cv.imshow("img",img)
   
button = Button(window,text="Display an Image",command=click,bg="white",fg="black",activeforeground='black',activebackground='white',compound="top",state=ACTIVE)
button.place(x=50,y=50)
button.pack()

window.mainloop() #places window on screen, listens for events

