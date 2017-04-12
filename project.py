import random

def fcfs():
	n = random.randint(3,10)
	arrivalTime = [i for i in range(n)]
	execTime = [random.randint(1,10) for i in range(n)]
	process = ['P'+str(i) for i in range(n)]
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

	print arrivalTime
	print process
	print execTime
	print burstTime

def sjn():
	n = random.randint(3,10)
	arrivalTime = [i for i in range(n)]
	execTime = [random.randint(1,10) for i in range(n)]
	process = ['P'+str(i) for i in range(n)]
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

	print arrivalTime
	print process
	print execTime
	print burstTime

def pbs():
	n = random.randint(3,10)
	arrivalTime = [i for i in range(n)]
	execTime = [random.randint(1,10) for i in range(n)]
	process = ['P'+str(i) for i in range(n)]
	priority = [random.randint(0,n) for i in range(n)]
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

	print arrivalTime
	print process
	print execTime
	print burstTime
	print priority


def srt():
	n = random.randint(3,10)
	arrivalTime = [i for i in range(n)]
	execTime = [random.randint(1,10) for i in range(n)]
	process = ['P'+str(i) for i in range(n)]
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

	print arrivalTime
	print process
	print execTime
	print burstTime

def rr():
	n = random.randint(3,10)
	arrivalTime = [i for i in range(n)]
	execTime = [random.randint(1,10) for i in range(n)]
	process = ['P'+str(i) for i in range(n)]
	quantom = random.randint(2,5)
	burstTime = [0 for _ in range(n)]
	d = arrivalTime[:]
	e = execTime[:]
	p = process[:]
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
	print arrivalTime
	print process
	print execTime
	print burstTime
	print quantom

def ltr():
	n = random.randint(3,10)
	arrivalTime = [i for i in range(n)]
	execTime = [random.randint(1,10) for i in range(n)]
	process = ['P'+str(i) for i in range(n)]
	burstTime = [0 for _ in range(n)]
	d = arrivalTime[:]
	e = execTime[:]
	execOrder = list()
	while len(d) > 0:
		curr = random.randint(0,len(d)-1)
		print curr 
		print d
		for i in d:
			burstTime[i] += e[curr]
		execOrder.append('P' +str(d[curr]))
		del d[curr]
		del e[curr]
	print arrivalTime
	print process
	print execTime
	print burstTime
	print execOrder

def mlq():
	n1 = random.randint(3,10)
	arrivalTime1 = [i for i in range(n1)]
	execTime1 = [random.randint(1,10) for i in range(n1)]
	process1 = ['P'+str(i) for i in range(n1)]
	burstTime1 = [0 for _ in range(n1)]
	n2 = random.randint(3,10)
	arrivalTime2 = [i for i in range(n2)]
	execTime2 = [random.randint(1,10) for i in range(n2)]
	process2 = ['P'+str(i) for i in range(n2)]
	burstTime2 = [0 for _ in range(n2)]
	d1 = arrivalTime1[:]
	e1 = execTime1[:]
	d2 = arrivalTime2[:]
	e2 = execTime2[:]
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
	waitTime1 = [burstTime1[i]-arrivalTime1[i]-execTime1[i] for i in range(n1)]
	for i in range(len(waitTime1)):
		if waitTime1[i] < 0:
			waitTime1[i] = 0
	waitTime2 = [burstTime2[i]-arrivalTime2[i]-execTime2[i] for i in range(n2)]
	for i in range(len(waitTime2)):
		if waitTime2[i] < 0:
			waitTime2[i] = 0
	avg1 = sum(waitTime1)/float(len(waitTime1))
	avg2 = sum(waitTime2)/float(len(waitTime2))
	
if __name__ == '__main__':
	ltr()