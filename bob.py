# Author Ashish
# Usage BOB QKD GUI
# Version 1
# Basic GUI version with all the buttons for the controls


from tkinter import *
import tkinter as tk
from tkinter import ttk


def setup():
    Frame1 = Frame(Output_Frame)
    Frame1.pack(side=TOP)

    Detectorlabel = Label(Frame1, text='Detector-1 characteristics', font=("Times New Roman", 20))
    Detectorlabel.pack(side=LEFT)

    Setup_DetectorBt = Button(Frame1, text='Setup Detector-1', command=setupdetector, bg="orange",fg="black",font="Times 16")
    Setup_DetectorBt.pack(side =LEFT,fill="both")

    OnInput = Entry(Output_Frame, text="Enter the on time", width=32)  # the width refers to the number of characters                     
    OnInput.pack()
    OnInput.get()
    
    Setup_OntimeBt = Button(Output_Frame, text='On Time', command=Ontime, height=4, width=23)
    Setup_OntimeBt.pack()

    OffInput = Entry(Output_Frame, text="Enter the off time", width=32)  # the width refers to the number of characters
    OffInput.pack()
    OffInput.get()

    Setup_OfftimeBt = Button(Output_Frame, text='Off Time', command=Offtime, height=4, width=23)
    Setup_OfftimeBt.pack()

    VoltageInput = Entry(Output_Frame, text="Enter the threshold voltage", width=32)  # the width refers to the number of characters
    VoltageInput.pack()
    VoltageInput.get()
    
    Setup_thresholdvoltageBt = Button(Output_Frame, text='Threshold Voltage', command=thresholdvoltage, height=4, width=23)
    Setup_thresholdvoltageBt.pack()

   Detectorlabel = Label(Frame2, text='Detector-2 characteristics', font=("Times New Roman", 20))
    Detectorlabel.pack(side=LEFT)

    Setup_DetectorBt = Button(Frame2, text='Setup Detector-2', command=setupdetector, bg="orange",fg="black",font="Times 16")
    Setup_DetectorBt.pack(side =LEFT,fill="both")

    OnInput = Entry(Output_Frame, text="Enter the on time-2", width=32)  # the width refers to the number of characters                     
    OnInput.pack()
    OnInput.get()
    
    Setup_OntimeBt = Button(Output_Frame, text='On Time', command=Ontime, height=2, width=23)
    Setup_OntimeBt.pack()

    OffInput = Entry(Output_Frame, text="Enter the off time-2", width=32)  # the width refers to the number of characters
    OffInput.pack()
    OffInput.get()

    Setup_OfftimeBt = Button(Output_Frame, text='Off Time', command=Offtime, height=2, width=23)
    Setup_OfftimeBt.pack()

    VoltageInput = Entry(Output_Frame, text="Enter the threshold voltage-2", width=32)  # the width refers to the number of characters
    VoltageInput.pack()
    VoltageInput.get()
    
    Setup_thresholdvoltageBt = Button(Output_Frame, text='Threshold Voltage', command=thresholdvoltage, height=2, width=23)
    Setup_thresholdvoltageBt.pack()

    Frame3 = Frame(Output_Frame)
    Frame3.pack(side=TOP)
    
    DliBiaslabel = Label(Frame3, text='Enter the DLI Bias', font=("Times New Roman", 20))
    DliBiaslabel.pack(side=LEFT)
    
    Bias = Entry(Output_Frame, text="Enter the DLI Bias", width=32)  # the width refers to the number of characters                     
    Bias.pack()
    Bias.get()
    
    Setup_BiasBt = Button(Output_Frame, text='DLI Bias', command=dlibias, height=2, width=23)
    Setup_BiasBt.pack()
    return

def setupdetector():
    return

def Ontime():
    return

def Offtime():
    return

def thresholdvoltage():
    return

def Authenticate():
    return

def dlibias():
    return

def set_key():
    return


def get_key():
    return

def ldpcdecoder():
    return

def securekey():
    return

## main frame
Root = Tk()
Root.title('BOB QKD SYSTEM')
Root.minsize(500, 420)
Root.maxsize(1444, 881)
Root.configure(bg="black")
Root.resizable(1, 1)
##WIDTH = 1000
##HEIGHT = 800
##Root.geometry("1000x800")

## Title frame
Title_Frame = Frame(Root, borderwidth=4, relief="flat")
Title_Frame.place(relx=0.016, rely=0.049, relheight=0.16, relwidth=0.982)
Title_Frame.configure(bg="white")

## IIT M Logo
imageEx = PhotoImage(file='iitm.png')
img = imageEx.zoom(14)
img = img.subsample(32)
Label(Title_Frame, image=img).pack(side=LEFT, expand=True)
## Title
title = Label(Title_Frame, text='BOB(RECEIVER)', font="Times 35")
title.pack(fill="both", side=LEFT, expand=True)
title.configure(bg="orange", fg="black")

## Process setup frame
Process_Frame = Frame(Root)
Process_Frame.place(relx=0.016, rely=0.222, relheight=0.767, relwidth=0.364)

## Adding buttons to the process frame
bt0 = Button(Process_Frame, text='Setup', command=setup, bg='orange', font="Times 20")
bt1 = Button(Process_Frame, text='Authenticate', command=Authenticate, bg='orange', font="Times 20")
bt2 = Button(Process_Frame, text='Receive raw key', command=get_key, bg='orange', font="Times 20")
bt3 = Button(Process_Frame, text='Send sifted key', command=set_key, bg='orange', font="Times 20")
bt4 = Button(Process_Frame, text='LDPC decoding', command=ldpcdecoder, bg='orange', font="Times 20")
bt5 = Button(Process_Frame, text='Secure key', command=securekey, bg='orange', font="Times 20")

bt0.pack(fill="both")
bt1.pack(fill="both")
bt2.pack(fill="both")
bt3.pack(fill="both")
bt4.pack(fill="both")
bt5.pack(fill="both")


## Output frame
Output_Frame = Frame(Root)
Output_Frame.place(relx=0.388, rely=0.222, relheight=0.767, relwidth=0.607)

Root.mainloop()
