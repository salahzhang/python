from check import (
	is_valid_in_first,
	is_valid_in_second,
	is_valid_in_third,
)
from process import(
	processed1,
	processed2,
	processed3,
)
# from test import test
#author: Si Zhang

#################
# Read data.in ##
#################
f = open("data.in",'r')

errors = []
entries = []
cnt = 0

l = f.readline()
while l:
	entry_info = l.split(', ')
	entry_info[-1] = entry_info[-1].replace('\n','')
	print entry_info
	if len(entry_info) == 5:
		if is_valid_in_first(entry_info):
			entries.append(processed1(entry_info))
		elif is_valid_in_third(entry_info):
			entries.append(processed3(entry_info))
		else:
			errors.append(cnt)
	elif len(entry_info) == 4:
		if is_valid_in_second(entry_info):
			entries.append(processed2(entry_info))
		else:
			errors.append(cnt)
	else:
		errors.append(cnt)
	cnt += 1
	print entries
	print errors
	l = f.readline()


#TODO: the keys should be sorted in ascending order

#################################
# write results in results.out ##
#################################
# results = open("results.out", "w")
# print {
# 	"entries": entries,
# 	"errors": errors
# }
# export.close()





import re
def is_phone(phonenum):
	phone_re = re.search('\D?\d{3}\D{0,2}\d{3}\D{0,1}\d{4}', phonenum)
	if not phone_re:
		return False
	return True


def is_zip(code):
	if not code.isdigit() or len(code) != 5:
		return False
	return True
	

def is_valid_in_first(line):
	if not line[0].isalpha() or not line[1].isalpha() or not is_phone(line[2]) or not line[3].isalpha() or not is_zip(line[4]):
		return False
	return True


def is_valid_in_second(line):
	name = line[0].split()
	if len(name) != 2:
		return False
	if not name[0].isalpha() or not name[1].isalpha() or not line[1].isalpha() or not is_zip(line[2]) or not is_phone(line[3]):
		return False
	return True

	
def is_valid_in_third(line):
	if not line[0].isalpha() or not line[1].isalpha() or not is_zip(line[2]) or not is_phone(line[3]) or not line[4].isalpha():
		return False
	return True




def processed1(line):
	phonenumber = line[2].replace('(','')
	phonenumber = phonenumber.replace(')','')
	return {
	"color":line[3],
	"firstname":line[1],
	"lastname":line[0],
	"phonenumber":phonenumber,
	"zipcode":line[4]
	}

def processed2(line):
	name = line[0].split()
	return {
	"color":line[1],
	"firstname":name[0],
	"lastname":name[1],
	"phonenumber":line[3].replace(' ','-'),
	"zipcode":line[2]
	}

def processed3(line):
	return {
	"color":line[4],
	"firstname":line[0],
	"lastname":line[1],
	"phonenumber":line[3].replace(' ','-'),
	"zipcode":line[2]
	}





from check import (
	is_valid_in_first,
	is_valid_in_second,
	is_valid_in_third,
)
from process import(
	processed1,
	processed2,
	processed3,
)
# entries = []
# errors = []
# cnt = 0
def test(l):
	entries=[]
	errors=[]
	cnt=0
	line = l.split(', ')
	line[-1].replace('\n','')
	if len(line) == 5:
		if is_valid_in_first(line):
			entries.append(processed1(line))
		elif is_valid_in_third(line):
			entries.append(processed3(line))
		else:
			errors.append(cnt)
	if len(line) == 4:
		if is_valid_in_second(line):
			entries.append(processed2(line))
		else:
			errors.append(cnt)
	return entries if entries else errors
print(test('Annalee, Loftis, 97296, 905 329 2054, blue'))
