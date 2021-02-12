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

    Detectorlabel1 = Label(Frame1, text='Detector-1 characteristics', font=("Times New Roman", 20))
    Detectorlabel1.pack(side=LEFT)

    Setup_Detector1Bt = Button(Frame1, text='Setup Detector-1', command=setupdetector1, bg="orange",fg="black",font="Times 16")
    Setup_Detector1Bt.pack(side =LEFT,fill="both")

    Setup_Ontime_label1 = Label(Output_Frame, text='On-Time',height=1, width=23)
    Setup_Ontime_label1.pack()

    global OnInput1
    global OffInput1
    global VoltageInput1
    OnInput1 = Entry(Output_Frame, text="Enter the on time-1", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    OnInput1.pack()
    
    Setup_Offtime_label1 = Label(Output_Frame, text='Off-Time', height=1, width=23)
    Setup_Offtime_label1.pack()

    OffInput1 = Entry(Output_Frame, text="Enter the off time-1", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters
    OffInput1.pack()

    Setup_thresholdvoltage_label1 = Label(Output_Frame, text='Threshold-Voltage', height=1, width=23)
    Setup_thresholdvoltage_label1.pack()

    VoltageInput1 = Entry(Output_Frame, text="Enter the threshold voltage-1", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters
    VoltageInput1.pack()

    Frame2 = Frame(Output_Frame)
    Frame2.pack(side=TOP)

    Detectorlabel2 = Label(Frame2, text='Detector-2 characteristics', font=("Times New Roman", 20))
    Detectorlabel2.pack(side=LEFT)

    Setup_Detector2Bt = Button(Frame2, text='Setup Detector-2', command=setupdetector2, bg="orange",fg="black",font="Times 16")
    Setup_Detector2Bt.pack(side =LEFT,fill="both")

    Setup_Ontime_label2 = Label(Output_Frame, text='On-Time', height=1, width=23)
    Setup_Ontime_label2.pack()
    
    global OnInput2
    global OffInput2
    global VoltageInput2
    OnInput2 = Entry(Output_Frame, text="Enter the on time-2", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    OnInput2.pack()

    Setup_Offtime_label2 = Label(Output_Frame, text='Off-Time', height=1, width=23)
    Setup_Offtime_label2.pack()

    OffInput2 = Entry(Output_Frame, text="Enter the off time-2", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters
    OffInput2.pack()

    Setup_thresholdvoltage_label2 = Label(Output_Frame, text='Threshold-Voltage',height=1, width=23)
    Setup_thresholdvoltage_label2.pack()

    VoltageInput2 = Entry(Output_Frame, text="Enter the threshold voltage-2", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters
    VoltageInput2.pack()

    Frame3 = Frame(Output_Frame)
    Frame3.pack(side=TOP)

    DliBias_label = Label(Frame3, text='DLI Bias', font=("Times New Roman", 20))
    DliBias_label.pack(side=LEFT)
    
    global Bias
    Bias = Entry(Output_Frame, text="DLI Bias", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    Bias.pack()

    Setup_DliBiasBt = Button(Frame3, text='Value', command= dlibias, bg="orange",fg="black",font="Times 16")
    Setup_DliBiasBt.pack(side =LEFT,fill="both")
    
    Frame4 = Frame(Output_Frame)
    Frame4.pack(side=TOP)
    
    GateLocation_label = Label(Frame4, text='Gate Location', font=("Times New Roman", 20))
    GateLocation_label.pack(side=LEFT)

    Setup_Location_label = Label(Output_Frame, text='Min-Delay', height=1, width=23)
    Setup_Location_label.pack()

    global mindelay
    global maxdelay
    global stepsize
    mindelay = Entry(Output_Frame, text="Enter the Min-Delay", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    mindelay.pack()
 
    Setup_Location_label = Label(Output_Frame, text='Max-Delay', height=1, width=23)
    Setup_Location_label.pack()

    maxdelay = Entry(Output_Frame, text="Enter the Max-Delay", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    maxdelay.pack()

    Setup_Location_label = Label(Output_Frame, text='Step-Size',height=1, width=23)
    Setup_Location_label.pack()

    stepsize = Entry(Output_Frame, text="Enter the Step-Size", width=32,font=("Arial",16), fg="red" )  # the width refers to the number of characters                     
    stepsize.pack()

    Setup_LocationBt = Button(Frame4, text ='Run', command = gatelocation, bg="orange",fg="black",font="Times 16")
    Setup_LocationBt.pack(side =LEFT,fill="both")
    return

def setupdetector1():
    s1 = float(OnInput1.get())
    print(s1)
    
    s2 = float(OffInput1.get())
    print(s2)
    
    s3 = float(VoltageInput1.get())
    print(s3)
    return

def setupdetector2():
    p1 = float(OnInput2.get())
    print(p1)
    
    p2 = float(OffInput2.get())
    print(p2)
    
    p3 = float(VoltageInput2.get())
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
    b = float(Bias.get())
    print(b)
    return

def gatelocation():
    g1 = float(mindelay.get())
    print(g1)
    
    g2 = float(maxdelay.get())
    print(g2)
    
    g3 = float(stepsize.get())
    print(g3)
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

