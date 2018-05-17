from tkinter import *
import pandas as pd

def pdcsv(data):
	df = pd.DataFrame(data, columns = ['ID','Password','KeepLoggedIn'])
	df.to_csv('out.csv')
	print (df)

def window():
	root = Tk()

	chb = IntVar()
	label_1 = Label(root, text = "Username")
	label_2 = Label(root, text = "Password")
	entry_1 = Entry(root)
	entry_2 = Entry(root)
	ch = Checkbutton(root, text = "Keep me logged in", variable = chb)
	b1 = Button(root, text  ="Login")
	b2 = Button(root, text  ="Sign Up", command = lambda: pdcsv([[entry_1.get(), entry_2.get(), chb.get()]]))


	label_1.grid(row=0, sticky = E)
	label_2.grid(row=1)

	entry_1.grid(row = 0, column = 1)
	entry_2.grid(row = 1, column = 1)

	ch.grid(columnspan = 2)

	b1.grid(row = 3)
	b2.grid(row = 3, column = 1)

	root.mainloop()
	
window()