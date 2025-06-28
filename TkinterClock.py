import tkinter
import tkinter.ttk
import tkinter.messagebox
#import tkinter.font #might be used in the future
import time
#import pyperclip #Used for clipboards

def _AddZero(Int:int, Digits:int=2) -> str: #Used in TimeGetter()
    Output = Int
    Zeros = Digits-len(str(Int))
    if len(str(Int)) <= Digits:
        Output = f"{'0'*Zeros}{Int}"
    return Output

def TimeGetter() -> tuple[int, str]: #Returns seconds in the year so far
    # Returns a tuple:
    # seconds in the year so far as a integer at index 0
    # seconds in the year so far printed nicely for console with colons as a string at index 1
    yday = time.localtime().tm_yday
    hour = time.localtime().tm_hour
    min = time.localtime().tm_min
    sec = time.localtime().tm_sec
    Console = f"{_AddZero(yday, 3)}:{_AddZero(hour)}:{_AddZero(min)}:{_AddZero(sec)}"
    
    #_AddZero((((((yday*24)+hour)*60)+min)*60)+sec, 8)
    
    hour = yday*24+hour
    min = hour*60+min
    sec = min*60+sec
    sec = _AddZero(sec, 8)
    return (sec,
        Console)

def FutureTimeGetter(day:int=0, hour:int=0, min:int=0, sec:int=0) -> int:
    day = time.localtime().tm_yday+day
    hour = time.localtime().tm_hour+hour
    min = time.localtime().tm_min+min
    sec = time.localtime().tm_sec+sec
    return (((((day*24)+hour)*60)+min)*60)+sec


def Quit() -> None:
    global root, QuitVar, ThreadBreak
    Input = tkinter.messagebox.askokcancel("Quit?","Are you sure you wanna quit?")
    if Input:
        root.destroy()
        QuitVar = 1 #stops the while loop

"""
def Copy():
    global TimeNow
    pyperclip.copy()
"""

def Stop() -> None:
    global Button1, StopVar
    if StopVar == 2: #intro
        FrameSeconds.pack(side="top")
        Mess2.pack(side='left')
        #Button2.pack(side="right")
        Mess3.pack(side='top')
        Mess.pack(side='top')
        Button1.pack(side="bottom")
        StopVar = 1
        Button1['text'] = "Stop"
        MessVar1.set(TimeGetter()[1])
        root.wm_maxsize(width=600,height=200)
        root.wm_minsize(width=490,height=170)
    elif StopVar:
        Button1['text'] = "Start?"
        MessVar2.set("Program stopped, waiting to start.")
        StopVar = 0
    elif not StopVar:
        Button1['text'] = "Stop"
        MessVar1.set(TimeGetter()[1])
        StopVar = 1

root = tkinter.Tk()
#root.geometry("497x157")
root.title( "Days to Seconds Clock")
root.protocol("WM_DELETE_WINDOW", Quit)
MessVar1 = tkinter.StringVar() #Time; Day of the year : Hour of the day : Minute of the hour : Second of the minute
MessVar2 = tkinter.StringVar() #Second of the year
MessVar3 = tkinter.StringVar() #Todays Date
Mess = tkinter.Label(root, textvariable=MessVar1, font=("Arial", 60, "bold"))
FrameSeconds = tkinter.ttk.Frame(root)
Mess2 = tkinter.Label(FrameSeconds, textvariable=MessVar2, font=("Arial"))
Mess3 = tkinter.Label(root, textvariable=MessVar3, font=("Arial"))
Button1 = tkinter.ttk.Button(root, text="Start", command=Stop)
#Button2 = tkinter.ttk.Button(FrameSeconds, text="Click to Copy", command=lambda: Copy())
#Button3 = tkinter.ttk.Button(root, text="12 Hour", command=Stop)
root.geometry(f'500x200+{int(root.winfo_screenwidth()/2)}+{int(root.winfo_screenheight()/2)}')
Button1.pack(ipadx=100, ipady=12, expand=True)

StopVar = 2
QuitVar = 0
#ThreadBreak = False
MessVar3.set(time.strftime("It is currently %A, %B %m of %Y"))
Counter = 0

while QuitVar == 0:
    root.update()
    if StopVar == 1:
        TimeNow = TimeGetter()
        MessVar1.set(TimeNow[1])
        MessVar2.set(f"Current Second of the Year: {TimeNow[0]}")
        Counter += 1
        if not Counter%60:
            Mess2.after(10000, MessVar3.set, time.strftime("It is currently %A, %B %m of %Y")) #if its 11:59 and then its 12am this should change the date
            Counter = 0
    #print(root.winfo_width(), root.winfo_height())
    time.sleep(.5)
    
