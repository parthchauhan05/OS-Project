from Tkinter import *
import random

def app():
	def unpack_all():
		c.pack_forget()
		fcfs.pack_forget()
		srt.pack_forget()
	 	sjn.pack_forget()
	 	pbs.pack_forget()
	 	rr.pack_forget()
	 	ltr.pack_forget()
	 	mlq.pack_forget()
	 	l1.pack_forget()
	 	l2.pack_forget()
	 	l3.pack_forget()
	 	l4.pack_forget()
	 	l5.pack_forget()
	 	l6.pack_forget()
	 	l7.pack_forget()
	 	destroy.pack_forget()

	def fcfs():
		unpack_all()
		n = random.randint(3,10)
		arrivalTime = [i for i in range(n)]
		execTime = [random.randint(1,10) for i in range(n)]
		process = ['P'+str(i) for i in range(n)]
		f.pack()
		Label(f,text = "\nFirst Come First Serve\n",font = ('Helveltika bold',12)).pack()
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)
		Label(f,text = "Burst Time:  "+ str(execTime)).pack(anchor = W)
		for i in range(n):
			for j in range(i,n):
				if arrivalTime[i] > arrivalTime[j]:
					temp = arrivalTime[i]
					arrivalTime[i] = arrivalTime[j]
					arrivalTime[j] = temp
					temp = execTime[i]
					execTime[i] = execTime[j]
					execTime[j] = temp
					temp = process[i]
					process[i] = process[j]
					process[j] = temp
		burstTime = list()
		burstTime.append(execTime[0]+arrivalTime[0])
		for i in range(1,n):
			burstTime.append(execTime[i]+burstTime[i-1])
		waitTime = [burstTime[i]-arrivalTime[i]-execTime[i] for i in range(n)]
		for i in range(len(waitTime)):
			if waitTime[i] < 0:
				waitTime[i] = 0
		avg = sum(waitTime)/n
		Label(f,text = "\n----- After Performing First Come First Serve Scheduling Algorithm -----\n").pack(anchor = W)
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)
		Label(f,text = "Burst Time:  "+ str(execTime)).pack(anchor = W)
		Label(f,text = "Turn Around Time:  "+ str(burstTime)).pack(anchor = W)
		Label(f,text = "Wait Time:  "+ str(waitTime)).pack(anchor = W)
		Label(f,text = "Average Wait Time: "+ str(avg)).pack(anchor = W)
		runOther.pack(padx = 120, side = LEFT)
		destroy.pack(padx = 10, side = LEFT)

	def sjn():
		unpack_all()
		n = random.randint(3,10)
		arrivalTime = [i for i in range(n)]
		execTime = [random.randint(1,10) for i in range(n)]
		process = ['P'+str(i) for i in range(n)]
		f = Frame(root)
		f.pack()
		Label(f,text = "\nShortest Job First\n",font = ('Helveltika bold',12)).pack()
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Run Time:  "+ str(execTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)
		for i in range(n):
			for j in range(i,n):
				if execTime[i] > execTime[j]:
					temp = arrivalTime[i]
					arrivalTime[i] = arrivalTime[j]
					arrivalTime[j] = temp
					temp = execTime[i]
					execTime[i] = execTime[j]
					execTime[j] = temp
					temp = process[i]
					process[i] = process[j]
					process[j] = temp
		burstTime = list()
		burstTime.append(execTime[0]+arrivalTime[0])
		for i in range(1,n):
			burstTime.append(execTime[i]+burstTime[i-1])
		waitTime = [burstTime[i]-arrivalTime[i]-execTime[i] for i in range(n)]
		for i in range(len(waitTime)):
			if waitTime[i] < 0:
				waitTime[i] = 0
		avg = sum(waitTime)/n
		Label(f,text = "\n----- After Performing Shortest Job Next Scheduling Algorithm -----\n").pack(anchor = W)
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Run Time:  "+ str(execTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)
		# Label(f,text = "Burst Time:  "+ str(execTime)).pack(anchor = W)
		Label(f,text = "Turn Around Time:  "+ str(burstTime)).pack(anchor = W)
		Label(f,text = "Wait Time:  "+ str(waitTime)).pack(anchor = W)
		Label(f,text = "Average Wait Time: "+ str(avg)).pack(anchor = W)
		runOther.pack(padx = 120, side = LEFT)
		destroy.pack(padx = 10, side = LEFT)

	def pbs():
		unpack_all()
		n = random.randint(3,10)
		arrivalTime = [i for i in range(n)]
		execTime = [random.randint(1,10) for i in range(n)]
		process = ['P'+str(i) for i in range(n)]
		priority = [random.randint(0,n) for i in range(n)]
		f = Frame(root)
		f.pack()
		Label(f,text = "\nPriority Based Scheduling\n",font = ('Helveltika bold',12)).pack()
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)
		Label(f,text = "Priority:  "+ str(priority)).pack(anchor = W)
		Label(f,text = "Run Time:  "+ str(execTime)).pack(anchor = W)
		
		for i in range(n):
			for j in range(i,n):
				if priority[i] < priority[j]:
					temp = arrivalTime[i]
					arrivalTime[i] = arrivalTime[j]
					arrivalTime[j] = temp
					temp = execTime[i]
					execTime[i] = execTime[j]
					execTime[j] = temp
					temp = process[i]
					process[i] = process[j]
					process[j] = temp
					temp = priority[i]
					priority[i] = priority[j]
					priority[j] = temp
		burstTime = list()
		burstTime.append(execTime[0]+arrivalTime[0])
		for i in range(1,n):
			burstTime.append(execTime[i]+burstTime[i-1])
		waitTime = [burstTime[i]-arrivalTime[i]-execTime[i] for i in range(n)]
		for i in range(len(waitTime)):
			if waitTime[i] < 0:
				waitTime[i] = 0
		avg = sum(waitTime)/n
		Label(f,text = "\n----- After Performing Priority based Scheduling Algorithm -----\n").pack(anchor = W)
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)
		Label(f,text = "Run Time:  "+ str(execTime)).pack(anchor = W)
		Label(f,text = "Priority:  "+ str(priority)).pack(anchor = W)
		Label(f,text = "Turn around Time:  "+ str(burstTime)).pack(anchor = W)
		Label(f,text = "Wait Time:  "+ str(waitTime)).pack(anchor = W)
		Label(f,text = "Average Wait Time: "+ str(avg)).pack(anchor = W)
		runOther.pack(padx = 120, side = LEFT)
		destroy.pack(padx = 10, side = LEFT)

	def srt():
		unpack_all()
		n = random.randint(3,10)
		arrivalTime = [i for i in range(n)]
		execTime = [random.randint(1,10) for i in range(n)]
		process = ['P'+str(i) for i in range(n)]
		f = Frame(root)
		f.pack()
		Label(f,text = "\nShortest Run Time Next\n",font = ('Helveltika bold',12)).pack()
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)
		Label(f,text = "Run Time:  "+ str(execTime)).pack(anchor = W)
		for i in range(n):
			for j in range(i,n):
				if execTime[i] > execTime[j]:
					temp = arrivalTime[i]
					arrivalTime[i] = arrivalTime[j]
					arrivalTime[j] = temp
					temp = execTime[i]
					execTime[i] = execTime[j]
					execTime[j] = temp
					temp = process[i]
					process[i] = process[j]
					process[j] = temp
		burstTime = list()
		burstTime.append(execTime[0]+arrivalTime[0])
		for i in range(1,n):
			burstTime.append(execTime[i]+burstTime[i-1])
		waitTime = [burstTime[i]-arrivalTime[i]-execTime[i] for i in range(n)]
		for i in range(len(waitTime)):
			if waitTime[i] < 0:
				waitTime[i] = 0
		avg = sum(waitTime)/n
		Label(f,text = "\n----- After Performing Shortest Run Time Next Scheduling Algorithm -----\n").pack(anchor = W)
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)
		Label(f,text = "Run Time:  "+ str(execTime)).pack(anchor = W)
		# Label(f,text = "Burst Time:  "+ str(execTime)).pack(anchor = W)
		Label(f,text = "Turn Around Time:  "+ str(burstTime)).pack(anchor = W)
		Label(f,text = "Wait Time:  "+ str(waitTime)).pack(anchor = W)
		Label(f,text = "Average Wait Time: "+ str(avg)).pack(anchor = W)
		runOther.pack(padx = 120, side = LEFT)
		destroy.pack(padx = 10, side = LEFT)	

	def rr():
		unpack_all()
		n = random.randint(3,10)
		arrivalTime = [i for i in range(n)]
		execTime = [random.randint(1,10) for i in range(n)]
		process = ['P'+str(i) for i in range(n)]
		quantom = random.randint(2,5)
		burstTime = [0 for _ in range(n)]
		d = arrivalTime[:]
		e = execTime[:]
		p = process[:]
		f = Frame(root)
		f.pack()
		Label(f,text = "\nRound Robin Schduling\n",font = ('Helveltika bold',12)).pack()
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)
		Label(f,text = "Quantom:  "+ str(quantom)).pack(anchor = W)
		Label(f,text = "Run Time:  "+ str(execTime)).pack(anchor = W)
		flag = False
		cnt = burstTime[:]
		while len(d) > 0:
			flag = True
			if e[0] > quantom :
				flag = False
				e[0] -= quantom
				e.append(e[0])
				p.append(p[0])
				d.append(d[0])
			del d[0]
			if flag:
				for i in d:
					cnt[i] += e[0]
			else:
				for i in d:
					cnt[i] += quantom
			del p[0]
			del e[0]
		for x in arrivalTime:
			t = execTime[x] % quantom 
			if t == 0:
				burstTime[x] = cnt[x] + quantom
			else :
				burstTime[x] = cnt[x] + t
		waitTime = [burstTime[i]-arrivalTime[i]-execTime[i] for i in range(n)]
		for i in range(len(waitTime)):
			if waitTime[i] < 0:
				waitTime[i] = 0
		avg = sum(waitTime)/n
		Label(f,text = "\n----- After Performing Round Robin Scheduling Algorithm -----\n").pack(anchor = W)
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)
		Label(f,text = "Quantom:  "+ str(quantom)).pack(anchor = W)
		Label(f,text = "Run Time:  "+ str(execTime)).pack(anchor = W)
		# Label(f,text = "Burst Time:  "+ str(execTime)).pack(anchor = W)
		Label(f,text = "Turn Around Time:  "+ str(burstTime)).pack(anchor = W)
		Label(f,text = "Wait Time:  "+ str(waitTime)).pack(anchor = W)
		Label(f,text = "Average Wait Time: "+ str(avg)).pack(anchor = W)
		runOther.pack(padx = 120, side = LEFT)
		destroy.pack(padx = 10, side = LEFT)

	def ltr():
		unpack_all()
		n = random.randint(3,10)
		arrivalTime = [i for i in range(n)]
		execTime = [random.randint(1,10) for i in range(n)]
		process = ['P'+str(i) for i in range(n)]
		burstTime = [0 for _ in range(n)]
		d = arrivalTime[:]
		e = execTime[:]
		execOrder = list()
		f = Frame(root)
		f.pack()
		Label(f,text = "\nLottery Schduling\n",font = ('Helveltika bold',12)).pack()
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)	
		Label(f,text = "Run Time:  "+ str(execTime)).pack(anchor = W)
		while len(d) > 0:
			curr = random.randint(0,len(d)-1)
			for i in d:
				burstTime[i] += e[curr]
			execOrder.append('P' +str(d[curr]))
			del d[curr]
			del e[curr]
		waitTime = [burstTime[i]-arrivalTime[i]-execTime[i] for i in range(n)]
		for i in range(len(waitTime)):
			if waitTime[i] < 0:
				waitTime[i] = 0
		avg = sum(waitTime)/n
		Label(f,text = "\n----- After Performing Lottery Scheduling Algorithm -----\n").pack(anchor = W)
		Label(f,text = "Arrival Time:  "+ str(arrivalTime)).pack(anchor = W)
		Label(f,text = "Process:  "+ str(process)).pack(anchor = W)	
		Label(f,text = "Run Time:  "+ str(execTime)).pack(anchor = W)
		# Label(f,text = "Burst Time:  "+ str(execTime)).pack(anchor = W)
		Label(f,text = "Turn Around Time:  "+ str(burstTime)).pack(anchor = W)
		Label(f,text = "Wait Time:  "+ str(waitTime)).pack(anchor = W)
		Label(f,text = "Average Wait Time: "+ str(avg)).pack(anchor = W)
		runOther.pack(padx = 120, side = LEFT)
		destroy.pack(padx = 10, side = LEFT)	

	def mlq():
		unpack_all()
		n = random.randint(3,10)
		arrivalTime1 = [i for i in range(n)]
		execTime1 = [random.randint(1,10) for i in range(n)]
		process1 = ['P'+str(i) for i in range(n)]
		burstTime1 = [0 for _ in range(n)]
		n = random.randint(3,10)
		arrivalTime2 = [i for i in range(n)]
		execTime2 = [random.randint(1,10) for i in range(n)]
		process2 = ['P'+str(i) for i in range(n)]
		burstTime2 = [0 for _ in range(n)]
		d1 = arrivalTime1[:]
		e1 = execTime1[:]
		d2 = arrivalTime2[:]
		e2 = execTime2[:]
		f.pack()
		Label(f,text = "\nMultiple Level Queue Scheduling\n",font = ('Helveltika bold',12)).pack()
		Label(f,text = "Arrival Time of CPU-Bound Processes:  "+ str(arrivalTime1)).pack(anchor = W)
		Label(f,text = "Process of CPU-Bound Processes:  "+ str(process1)).pack(anchor = W)
		Label(f,text = "Burst Time of CPU-Bound Processes:  "+ str(execTime1)).pack(anchor = W)
		Label(f,text = "Arrival Time of I/O-Bound Processes:  "+ str(arrivalTime2)).pack(anchor = W)
		Label(f,text = "Process of I/O-Bound Processes:  "+ str(process2)).pack(anchor = W)
		Label(f,text = "Burst Time of I/O-Bound Processes:  "+ str(execTime2)).pack(anchor = W)
		while len(d1)>0 or len(d2)>0:
			if len(d1) > 0:
				for i in d1:
					burstTime1[i] += e1[0]
				for i in d2:
					burstTime2[i] += e1[0]
				del d1[0]
				del e1[0]
			if len(d2) > 0:
				for i in d1:
					burstTime1[i] += e2[0]
				for i in d2:
					burstTime2[i] += e2[0]
				del d2[0]
				del e2[0]
		waitTime1 = [burstTime1[i]-arrivalTime1[i]-execTime1[i] for i in range(n)]
		for i in range(len(waitTime1)):
			if waitTime1[i] < 0:
				waitTime1[i] = 0
		waitTime2 = [burstTime2[i]-arrivalTime2[i]-execTime2[i] for i in range(n)]
		for i in range(len(waitTime2)):
			if waitTime2[i] < 0:
				waitTime2[i] = 0
		avg1 = sum(waitTime1)/len(waitTime1)
		avg2 = sum(waitTime2)/len(waitTime2)
		Label(f,text = "\n----- After Performing First Come First Serve Scheduling Algorithm -----\n").pack(anchor = W)
		Label(f,text = "Arrival Time of CPU-bound Processes:  "+ str(arrivalTime1)).pack(anchor = W)
		Label(f,text = "Process of CPU-bound Processes:  "+ str(process1)).pack(anchor = W)
		Label(f,text = "Burst Time of CPU-bound Processes:  "+ str(execTime1)).pack(anchor = W)
		Label(f,text = "Turn Around Time of CPU-bound Processes:  "+ str(burstTime1)).pack(anchor = W)
		Label(f,text = "Wait Time of CPU-bound Processes:  "+ str(waitTime1)).pack(anchor = W)
		Label(f,text = "Average Wait Time: "+ str(avg1)).pack(anchor = W)
		Label(f,text = "Arrival Time of I/O-bound Processes:  "+ str(arrivalTime2)).pack(anchor = W)
		Label(f,text = "Process of I/O-bound Processes:  "+ str(process2)).pack(anchor = W)
		Label(f,text = "Burst Time of I/O-bound Processes:  "+ str(execTime2)).pack(anchor = W)
		Label(f,text = "Turn Around Time of I/O-bound Processes:  "+ str(burstTime2)).pack(anchor = W)
		Label(f,text = "Wait Time of I/O-bound Processes:  "+ str(waitTime2)).pack(anchor = W)
		Label(f,text = "Average Wait Time: "+ str(avg2)).pack(anchor = W)
		runOther.pack(padx = 120, side = LEFT)
		destroy.pack(padx = 10, side = LEFT)	
		return


	root = Tk()
	root.title("Process Scheduling")
	Label(root,text = '').pack()
	destroy = Button(root,text = "Quit",command=quit)
	runOther = Button(root,text = "Run Other",command = app)
	f = Frame(root)
	f.pack()
	f.pack_forget()
	w = Label(root,text = "\n\tProcess Scheduling Algorithms Simulations\t",font = ('Helveltika bold',14))
	c = Label(root,text = "\nChoose any one from below:\n")
	w.pack()
	c.pack()
	fcfs = Button(root,text = "First Come First Serve", width = 20, command = fcfs)
	fcfs.pack(padx = 10)
	l1 = Label(root,text = '')
	l1.pack()
	sjn = Button(root,text = "Shortest Job First", width = 20, command = sjn)
	sjn.pack(padx = 10)
	l2 = Label(root,text = '')
	l2.pack()
	pbs = Button(root,text = "Priority Based Scheduling", width = 20, command = pbs)
	pbs.pack(padx = 10)
	l3 = Label(root,text = '')
	l3.pack()
	srt = Button(root,text = "Shortest Running Time", width = 20, command = srt)
	srt.pack(padx = 10)
	l4 = Label(root,text = '')
	l4.pack()
	rr = Button(root,text = "Round Robin Scheduling", width = 20, command = rr)
	rr.pack(padx = 10)
	l5 = Label(root,text = '')
	l5.pack()
	ltr = Button(root,text = "Lottery Scheduling", width = 20, command = ltr)
	ltr.pack(padx = 10)
	l6 = Label(root,text = '')
	l6.pack()
	mlq = Button(root,text = "Multi Level Queue Scheduling", width = 20, command = mlq)
	mlq.pack(padx = 10)
	l7 = Label(root,text = '')
	l7.pack()
	destroy.pack(padx = 10)
	root.mainloop()

if __name__ == '__main__':
	app()