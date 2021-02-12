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

    Setup_DetectorBt = Button(Frame1, text='Setup Detector-1', command=setupdetector1, bg="orange",fg="black",font="Times 16")
    Setup_DetectorBt.pack(side =LEFT,fill="both")

    Setup_Ontime_label = Label(Output_Frame, text='On-Time',height=1, width=23)
    Setup_Ontime_label.pack()

    OnInput = Entry(Output_Frame, text="Enter the on time", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    OnInput.pack()
    
    Setup_Offtime_label = Label(Output_Frame, text='Off-Time', height=1, width=23)
    Setup_Offtime_label.pack()

    OffInput = Entry(Output_Frame, text="Enter the off time", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters
    OffInput.pack()

    Setup_thresholdvoltage_label = Label(Output_Frame, text='Threshold-Voltage', height=1, width=23)
    Setup_thresholdvoltage_label.pack()

    VoltageInput = Entry(Output_Frame, text="Enter the threshold voltage", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters
    VoltageInput.pack()

    Frame2 = Frame(Output_Frame)
    Frame2.pack(side=TOP)

    Detectorlabel = Label(Frame2, text='Detector-2 characteristics', font=("Times New Roman", 20))
    Detectorlabel.pack(side=LEFT)

    Setup_DetectorBt = Button(Frame2, text='Setup Detector-2', command=setupdetector2, bg="orange",fg="black",font="Times 16")
    Setup_DetectorBt.pack(side =LEFT,fill="both")

    Setup_Ontime_label = Label(Output_Frame, text='On-Time', height=1, width=23)
    Setup_Ontime_label.pack()

    OnInput = Entry(Output_Frame, text="Enter the on time-2", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    OnInput.pack()
    OnInput.get()

    Setup_Offtime_label = Label(Output_Frame, text='Off-Time', height=1, width=23)
    Setup_Offtime_label.pack()

    OffInput = Entry(Output_Frame, text="Enter the off time-2", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters
    OffInput.pack()
    OffInput.get()
   
    Setup_thresholdvoltage_label = Label(Output_Frame, text='Threshold-Voltage',height=1, width=23)
    Setup_thresholdvoltage_label.pack()

    VoltageInput = Entry(Output_Frame, text="Enter the threshold voltage-2", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters
    VoltageInput.pack()
    VoltageInput.get()
    
    Frame3 = Frame(Output_Frame)
    Frame3.pack(side=TOP)

    DliBias_label = Label(Frame3, text='DLI Bias', font=("Times New Roman", 20))
    DliBias_label.pack(side=LEFT)
    
    Bias = Entry(Output_Frame, text="DLI Bias", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    Bias.pack()
    Bias.get()

    Setup_DliBiasBt = Button(Frame3, text='Value', command= dlibias, bg="orange",fg="black",font="Times 16")
    Setup_DliBiasBt.pack(side =LEFT,fill="both")
    
    Frame4 = Frame(Output_Frame)
    Frame4.pack(side=TOP)
    
    GateLocation_label = Label(Frame4, text='Gate Location', font=("Times New Roman", 20))
    GateLocation_label.pack(side=LEFT)

    Setup_Location_label = Label(Output_Frame, text='Min-Delay', height=1, width=23)
    Setup_Location_label.pack()
    
    mindelay = Entry(Output_Frame, text="Enter the Min-Delay", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    mindelay.pack()
    mindelay.get()

    Setup_Location_label = Label(Output_Frame, text='Max-Delay', height=1, width=23)
    Setup_Location_label.pack()

    maxdelay = Entry(Output_Frame, text="Enter the Max-Delay", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    maxdelay.pack()
    maxdelay.get()

    Setup_Location_label = Label(Output_Frame, text='Step-Size',height=1, width=23)
    Setup_Location_label.pack()

    stepsize = Entry(Output_Frame, text="Enter the Step-Size", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    stepsize.pack()
    stepsize.get()

    Setup_LocationBt = Button(Frame4, text ='Run', command = gatelocation, bg="orange",fg="black",font="Times 16")
    Setup_LocationBt.pack(side =LEFT,fill="both")
    return

def setupdetector1():
    s1 = OnInput.get()
    print(s1)
    
    s2 = OffInput.get()
    print(s2)
    
    s3 = VoltageInput.get()
    print(s3)
    return

def setupdetector2():
    p1 = OnInput.get()
    print(p1)
    
    p2 = OffInput.get()
    print(p2)
    
    p3 = VoltageInput.get()
    print(p3)
    return

def Ontime():
    return

def Offtime():
    return

def thresholdvoltage():
    return

def Authenticate():
    return

def set_key():
    return

def dlibias():
    print(f"{Bias.get()}")
    return

def gatelocation():
    print(f"{mindelay.get()}")
    print(f"{maxdelay.get()}")
    print(f"{stepsize.get()}")
    return

def mindelay():
    return

def maxdelay():
    return

def stepsize():
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
Root.minsize(500, 320)
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
