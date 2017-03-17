from Tkinter import *
def printtext():
	global e
	string = e.get()
	print string 

def process():
	e.pack()
	e.focus_set()
	b = Button(root,text = "OK",command = printtext)
	b.pack(side='bottom')

root = Tk()
root.title("Simalating Process Scheduling")
e = Entry()
b = Button(root,text = "button", command = process)
b.pack()
root.mainloop()