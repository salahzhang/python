import sys
import math
#author: Si Zhang
#Mon, 9/19/2016

##error rate
#read wholelabel
RealLabels = sys.argv[1]
f = open(RealLabels)
wholelabel = {}
l = f.readline()
while l != "":
	a = l.split()
	wholelabel[int(a[1])] = int(a[0])
	l = f.readline()
#print(wholelabel)

#read predicted_bales
PreLabels = sys.argv[2]
f = open(PreLabels)
predict_labels = {}
l = f.readline()
n = 0
while l != "":
	a = l.split()
	predict_labels[n] = [int(a[0]),int(a[1])]
	n += 1
	l = f.readline()
#print (predict_labels)

#error rate
t00 = 0
t01 = 0
t11 = 0
t10 = 0
for i in range(0, len(predict_labels), 1):
	if wholelabel.get(predict_labels[i][0])==0 and predict_labels[i][1]==0:
		t00 += 1
	if wholelabel.get(predict_labels[i][0])==0 and predict_labels[i][1]==1:
		t01 += 1
	if wholelabel.get(predict_labels[i][0])==1 and predict_labels[i][1]==1:
		t11 += 1
	if wholelabel.get(predict_labels[i][0])==1 and predict_labels[i][1]==0:
		t10 += 1
#print(t00,t01,t11,t10)
ber = (t01/(t01+t00)+t10/(t10+t11))/2
print("ber: ", ber)
