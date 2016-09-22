import sys
import math
#author: Si Zhang
#Mon, 9/19/2016

datafile = sys.argv[1]

f = open(datafile, "r")

data = []
i = 0
l = f.readline()
while l != '':
	a = l.split()
	l2 = []
	for j in range(0, len(a), 1):
		l2.append(float(a[j]))
	data.append(l2)
	l = f.readline()

rows = len(data)
cols = len(data[0])



#########################
# Read training labels ##
#########################
labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = [0, 0]
l = f.readline()
while l != "":
	a = l.split()
	#print(a)
	trainlabels[int(a[1])] = int(a[0])
	l = f.readline()
	n[int(a[0])] += 1

#print(data)
#print(trainlabels)
#print(n)

# means
m0 = []
m1 = []

for i in range(0, cols, 1):
	m0.append(1)
	m1.append(1)

for i in range(0, rows, 1):
	if trainlabels.get(i) is not None and trainlabels[i] == 0:
		for j in range(0, cols, 1):
			m0[j] = m0[j] + data[i][j]

	if trainlabels.get(i) is not None and trainlabels[i] == 1:
		for j in range(0, cols, 1):
			m1[j] = m1[j] + data[i][j]

for j in range(0, cols, 1):
	m0[j] /= n[0]
	m1[j] /= n[1]

#print(m0)
#print(m1)

#standards
s0 = [0]*cols
s1 = [0]*cols


for i in range(0, rows, 1):
	if trainlabels.get(i) is not None and trainlabels[i] == 0:
		for j in range(0, cols, 1):
			s0[j] += (data[i][j]-m0[j])*(data[i][j]-m0[j])

	if trainlabels.get(i) is not None and trainlabels[i] == 1:
		for j in range(0, cols, 1):
			s1[j] += (data[i][j]-m1[j])*(data[i][j]-m1[j])

for j in range(0, cols, 1):
	s0[j] /= n[0]
	s1[j] /= n[1]

#print(s0)
#print(s1)

#prediction


##classify
for i in range(0, rows, 1):
	if trainlabels.get(i) == None:
		d0 = 0
		d1 = 0
		for j in range(0, cols, 1):
			d0 += ((data[i][j]-m0[j])**2)/s0[j]
			d1 += ((data[i][j]-m1[j])**2)/s1[j]
		if(d0<d1):
			print(i,'0')	
		else:
			print(i,'1')
			
			





