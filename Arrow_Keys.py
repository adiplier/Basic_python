from tkinter import *
import pyautogui as keypy
import time

ww = Tk()

def bup():
	time.sleep(1)
	keypy.press('up')
	
def bleft():
	time.sleep(1)
	keypy.press('left')
	
def bright():
	time.sleep(1)
	keypy.press('right')

def bdown():
	time.sleep(1)
	keypy.press('down')	
	
wtopf = Frame(ww)
wbotf = Frame(ww)
wtopf.pack(side = TOP)
wbotf.pack(side = BOTTOM)

wl = Label(wtopf, text = "Arrow Keys", fg = "green")
wl.pack(side=TOP)

button1 = Button(wtopf, text = "^", fg="green", command = bup)
button2 = Button(wbotf, text = "<", fg="blue", command = bleft)
button3 = Button(wbotf, text = "V", fg="red", command = bdown)
button4 = Button(wbotf, text = ">", fg="blue", command = bright)

button1.pack()
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

ww.mainloop()

