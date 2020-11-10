numbers = [3,1,2,5,6,7,4,32,33,65,3,2,1,4,6,7,8,93,34,100,30,20,25,124,45,546,323,1,2,3,3,4,5,6,7,842,23,2,3,5]
def bubbleSort(numbers, order='ascending'):
	for i in range(len(numbers)):
		for j in range(len(numbers)):
			if order =='descending':
				if numbers[i] < numbers[j]:
					numbers[i],numbers[j] = numbers[j], numbers[i]
			else:
				if numbers[i] > numbers[j]:
					numbers[i],numbers[j] = numbers[j], numbers[i]

	return numbers
print(bubbleSort(numbers,'descending'))
print(bubbleSort(numbers))


#Ex 2
#encoding k -> m, o->q, e->g
text = 'g fmnc wms bgblr rpylqjyrc gr zw fylb.rfyrq ufyr amknsrcpq ypc dmp.bmgle gr gl zw fylb gq glcddgagclr ylb rfyr q ufw rfgq rcvr gq qm jmle.sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.’’'

def decipher(text):
	empty = ''
	for i in text: # a - z is 97 - 122
		if ord(i) >= 97 and ord(i) <=120:
			empty = empty + chr(ord(i)+2)
		elif ord(i) > 120 and ord(i) <= 122:
			empty = empty + chr(ord(i)-24)
		elif i == ' ':
			empty = empty + i
		else:
			empty = empty + ' '

	print(empty)


decipher(text)

import re

def findsmall(file):
	f = open(file, 'r')
	text = f.read()
	x = re.findall('[A-Z]{3}[a-z][A-Z]{3}', text) 
	lowerList = []
	for i in x:
		for j in i:
			if j.islower():
				lowerList.append(j)

	print(lowerList)
findsmall("../bigmess.txt")


def rotate(myList, num):
	return myList[num:] + myList[:num]

print(rotate(['a','b','c','d','e'],3))
print(rotate(['a','b','c','d','e'],-1))


def flip(myList):
	flipped =[]
	while len(myList) > 0:
		flipped.append(myList.pop())
	print(flipped)

flip([1,2,3,4,5,6,7,8,9,10,11,12])
flip(['a','b','c'])

#[a,a,a,a,b,b,b,c,a,a,d,d,e] -> [a,b,c,a,d,e]

def removeSome(myList):
	previous_value = None
	newList = []

	for x in myList:
		if x != previous_value:
			newList.append(x)
			previous_value = x

	
	return newList

print(removeSome(['a','a','a','a','a','a','b','b','b','c','a','a','d','d','d','d','e']))
print(removeSome([1,1,1,1,1,1,1,2,2,1,1,3,3,4]))


def combine(myList):
	previous = None
	newList = []

	for x in myList:
		if x != previous:
			new = []
			previous = x
			newList.append(new)
		new.append(x)
		#if new not in newList:
			
	return newList

print(combine([1,1,1,1,1,1,1,2,2,1,1,3,3,4,4,4,3,3,3,4,4,5,5,5,5,1,1,1,1,1,1,1]))
print(combine(['a','a','a','a','a','a','b','b','b','c','a','a','d','d','d','d','e','e','w','w','a','a','a','a']))				 

