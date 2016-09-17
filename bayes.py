def LoadDataSet():
	PosttingList = [['my','dog','has','flea', \
					 'problem','help','please' ],
					['maybe','not','take','take','him',\
					 'to','dog','park','stupid'],
					['my','dalmation','is','so','cute',\
					 'I','love','him'],
					['stop','posting','stupid','worthless','garbage'],
					['mr','licks','ate','my','steak','how',\
					 'to','stop','him'],
					['quit','buying','worthless','dog','food','stupid']]
	ClassVec = [0,1,0,1,0,1]
	return PosttingList,ClassVec


def CreatVocabList(DataSet):
	VocabSet = set([])
	for document in DataSet:
		VocabSet = VocabSet | set(document)
	return list(VocabSet)

def SetofWords2Vec(VocabList, InputSet):
	ReturnVec = [0]*len(VocabList)
	for word in InputSet:
		if word in VocabList:
			ReturnVec[VocabList.index(word)] = 1
		else:
			print("the word: %s is not in my Vocabulary!" % word)
	return ReturnVec

def TrainNBO(TrainMatrix, TrainCategory):
	import numpy
	NumTrainDocs = len(TrainMatrix)
	NumWords = len(TrainMatrix[0])
	pAbusive = sum(TrainCategory)/float(NumTrainDocs)
	p0Num = numpy.ones(NumWords)
	p1Num = numpy.ones(NumWords)
	p0Denum = 2.0
	p1Denum = 2.0
	for i in range(NumTrainDocs):
		if TrainCategory[i] == 1:
			p1Num += TrainMatrix[i]
			p1Denum += sum(TrainMatrix[i])
		else:
			p0Num += TrainMatrix[i]
			p0Denum += sum(TrainMatrix[i])
	p1Vect = numpy.log(p1Num/p1Denum)
	p0Vect = numpy.log(p0Num/p0Denum)
	return p0Vect,p1Vect,pAbusive

def ClassifyNB(Vec2Classify, p0Vec, p1Vec, pClass1):
	p1 = sum(Vec2Classify * p1Vec) + log(pClass1)
	p0 = sum(Vec2Classify * p0Vec) + log(1.0 - pClass1)
	if p1 > p0:
		return 1
	else:
		return 0

def TestingNB():
	from array import array
	listOPots,listClasses = LoadDataSet()
	myVocabList = CreatVocabList(listOPots)
	trainMat = []
	for postindocs in listOPots:
		trainMat.append(SetofWords2Vec(myVocabList, postindocs))
	p0v,p1v,pAb = TrainNBO(trainMat,listClasses)
	TestEntry = ['love','my','dalamation']
	ThisDoc = array(SetofWords2Vec(myVocabList, TestEntry))
	print(TestEntry,'classified as: ', ClassifyNB(ThisDoc, p0v, p1v, pAb))
	TestEntry = ['stupid','garbage']
	ThisDoc = array(SetofWords2Vec(myVocabList, TestEntry))
	print(TestEntry,'classified as: ', ClassifyNB(ThisDoc, p0v, p1v, pAb))


def BagodWords2VecMN(VocabList,InputSet):
	ReturnVec = [0]*len(VocabList)
	for word in InputSet:
		if word in VocabList:
			ReturnVec[VocabList.index(word)] += 1
	return ReturnVec
