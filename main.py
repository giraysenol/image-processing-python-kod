# Giray Şenol/181805079

import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure


mainWindow=tk.Tk()
mainWindow.geometry('650x350+750+200')
mainWindow.title('Giray Senol / 181805079')
mainWindow.resizable(False, False)

window=mainWindow

lbl_name= tk.Label(mainWindow, font='Sans 15 bold', text='Giray Şenol')
lbl_id= tk.Label(mainWindow, font='Sans 15 bold', text ='181805079')


def openImage():
    global filename
    filename = filedialog.askopenfilename(initialdir="C:/Users/Giray/Desktop", title= "Select A File", filetypes=(("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")))

    global image
    image = cv2.imread(filename)
    cv2.imshow("Image",image)

def openDesiredImage():

    global filename2
    filename2 = filedialog.askopenfilename(initialdir="C:/Users/Giray/Desktop", title="Select A File", filetypes=(
    ("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.*")))

    global image2
    image2 = cv2.imread(filename2)
    cv2.imshow("Image2", image2)


def histogram():

    img = cv2.imread(filename)
    img2 = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

    b, g, r = cv2.split(img)
    cv2.imshow("Blue", b)
    cv2.imshow("Green", g)
    cv2.imshow("Red", r)

    plt.subplot(2,1,1)
    plt.title("Normal Histogram")
    plt.ylabel('Pixel')
    plt.hist(img.ravel(), 256, [0, 256],color="yellow",rwidth=1)
    plt.subplot(2, 1, 2)
    plt.title("Grey Histogram")
    plt.ylabel('Pixel')
    plt.hist(img2.ravel(),256,[0,256],color="grey",rwidth=0.8)
    plt.show()
    #plt.hist(b.ravel(),256, [0,256])
    #plt.hist(r.ravel(),256, [0,256])
    #plt.hist(g.ravel(),256, [0,256])


def equalization():

    img = cv2.imread(filename,0)
    global equ1
    equ1=cv2.equalizeHist(img)


    res = np.hstack((img, equ1))
    plt.imshow(res, cmap="gray")
    plt.show()


def specification():

    src = cv2.imread(filename)
    ref = cv2.imread(filename2)

    multi = True if src.shape[-1] > 1 else False
    matched = exposure.match_histograms(src,ref,multichannel = multi)

    #horizontalAppendedImg = np.hstack((src, ref, matched))
    cv2.imshow("Specification", matched)



btn_Openimage = tk.Button(mainWindow,text="Open Image File",command=openImage)
btn_Desiredimage = tk.Button(mainWindow,text="Open Desired Image",command=openDesiredImage)
btn_Histogram = tk.Button(mainWindow,text="Histogram",command=histogram)
btn_Equalization = tk.Button(mainWindow,text="Equalization",command=equalization)
btn_Specification = tk.Button(mainWindow,text="Specification",command=specification)


lbl_name.pack(ipady=10)
lbl_id.pack(ipady=10)
btn_Specification.pack(side=tk.BOTTOM,fill=tk.X, ipady=5)
btn_Equalization.pack(side=tk.BOTTOM,fill=tk.X, ipady=5)
btn_Histogram.pack(side=tk.BOTTOM,fill=tk.X, ipady=5)
btn_Desiredimage.pack(side=tk.BOTTOM,fill=tk.X, ipady=5)
btn_Openimage.pack(side=tk.BOTTOM,fill=tk.X, ipady=5)
window.mainloop()

