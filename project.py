from Tkinter import *
def printtext():
	global e
	string = e.get()
	print string 

def process():
	b.destroy()
	e.grid(in_=window)
	e.pack()
	#e.focus_set()
	b2 = Button(window,text = "OK",command = printtext)
	b2.grid(in_=window)
	b2.pack(side='bottom')

root = Tk()
root.title("Simalating Process Scheduling")
window = Frame(root,width = 720, height = 480)
window.pack(fill=BOTH, expand = YES)
e = Entry()
b = Button(root,text = "button", command = process)
b.grid(in_=window)
b.pack()
root.mainloop()