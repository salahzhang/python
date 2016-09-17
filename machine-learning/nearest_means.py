import sys
import math


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

print("rows = ", rows, "cols = ", cols)

for i in range(0, rows, 1):
	print(data[i])

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
	print(a)
	trainlabels[int(a[1])] = int(a[0])
	l = f.readline()
	n[int(a[0])] += 1

print(data)
print(trainlabels)
print(n)

# means
m0 = []
m1 = []

for i in range(0, cols, 1):
	m0.append(0)
	m1.append(0)

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

print(m0)
print(m1)

# prediction
wholelabel = sys.argv[3]
f = open(wholelabel)

wholel = []
l = f.readline()
while l != '':
	wholel.append([l.split()[1], l.split()[0]])
	l = f.readline()

print(len(wholel))

labelfile = sys.argv[2]
f = open(labelfile)

trainl = []
l = f.readline()
while l != '':
	trainl.append(l.split()[1])
	l = f.readline()

print(len(trainl))

testl = []

for i in range(0, len(wholel), 1):
	if wholel[i][0] not in trainl:
		testl.append(wholel[i][0])

print(len(testl))
print(testl)

distance = []

for i in range(0, len(testl), 1):
	s0 = 0
	s1 = 0
	for j in range(0, len(testl[1]), 1):
		s0 += math.pow(float(data[int(testl[i])][j])-m0[j], 2)
		s1 += math.pow(float(data[int(testl[i])][j])-m1[j], 2)
	distance.append([int(testl[i]), math.sqrt(s0), math.sqrt(s1)])

print(distance)

predict_result = []
for i in range(0, len(testl), 1):
	if distance[i][1] > distance[i][2]:
		predict_result.append([distance[i][0], 1])
	elif distance[i][2] > distance[i][1]:
		predict_result.append([distance[i][0], 0])

print(predict_result)

# Truth result

truth_result = []

for i in range(0, len(testl), 1):
	truth_result.append([int(wholel[int(testl[i])][0]), int(wholel[int(testl[i])][1])])

print(truth_result)

# Balanced error rate
T0P0 = 0
T0P1 = 0
T1P0 = 0
T1P1 = 0

for i in range(0, len(truth_result), 1):
	if truth_result[i][1] == 0 and predict_result[i][1] == 0:
		T0P0 += 1
	elif truth_result[i][1] == 0 and predict_result[1][1] == 1:
		T0P1 += 1
	elif truth_result[i][1] == 1 and predict_result[1][1] == 0:
		T1P0 += 1
	elif truth_result[i][1] == 1 and predict_result[1][1] == 1:
		T1P1 += 1

ber = 1/2*(T0P1/(T0P1+T0P0)+T1P0/(T1P0+T1P1))
print(ber)