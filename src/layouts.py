from tkinter import ttk
from PIL import Image,ImageTk
import tkinter as tk
import cv2 as cv
import easygui

class MainMenu:
    image = None
    def __init__(self, master):
        def ChangeFrame(frame):
            frame.tkraise()
        

        mainMenuFrame = ttk.Frame(master)
        secondMenuFrame = ttk.Frame(master)

        for frame in (mainMenuFrame,secondMenuFrame):
            frame.grid(row=0,column=0,sticky='nsew')

        #==========Main Menu Frame
        btnLoadImg = ttk.Button(mainMenuFrame,text='Load image',command=self.LoadImage)
        btnLoadImg.pack(side=tk.LEFT)

        btnShow = ttk.Button(mainMenuFrame,text='Show image', command=self.ShowImage)
        btnShow.pack(side =tk.LEFT)

        btnExit = ttk.Button(mainMenuFrame,text='Quit',command=lambda: exit())
        btnExit.pack(side =tk.LEFT)

        btnSecondMenu = ttk.Button(mainMenuFrame,text='Second menu',command=lambda: ChangeFrame(secondMenuFrame))
        btnSecondMenu.pack(side=tk.BOTTOM)

        #=========Second Menu Frame
        btnMainMenu = ttk.Button(secondMenuFrame,text='Main menu',command=lambda: ChangeFrame(mainMenuFrame))
        btnMainMenu.pack(side=tk.BOTTOM)
        
        ChangeFrame(mainMenuFrame)
    
    def LoadImage(self):
        filePath = easygui.fileopenbox()
        self.image = cv.imread(filePath)
        self.ShowImage()
    
    def ShowImage(self):
        cv.imshow('Image preview',self.image)
        cv.waitKey(0)
        cv.destroyAllWindows()
