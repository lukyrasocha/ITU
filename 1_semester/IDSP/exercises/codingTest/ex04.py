def isEven(myList):
	if len(myList) == 0:
		return 0
	if myList[0] % 2 == 0:
		return 1 + isEven(myList[1:])
	else:
		return 0 + isEven(myList[1:])

print(isEven([1,2,3,4,5,6,8,8,8,9]))

def printType(myList):
	if len(myList) == 0:
		return
	else:
		print((myList[0],type(myList[0])))
		return printType(myList[1:])

print(printType([1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12] ]
))

def printNum(num):
	x = num
	if x == 7:
		return
	if x == 3 or x == 5:
		return printNum(num+1)
	else:
		print(x)
		return printNum(num+1)

	
printNum(0)
evenList = []
def isEven2(num):

	if num == 401:
		return evenList

	x = list(str(num))
	if len(x) == 1:
		if int(x[0]) % 2 == 0:
			evenList.append(num)
			
	if len(x) == 2:
		if int(x[0]) % 2 == 0 and int(x[1]) % 2 ==0:
			evenList.append(num)
			

	if len(x) == 3:
		if int(x[0]) % 2 == 0 and int(x[1]) % 2 ==0 and int(x[2]) % 2 ==0:
			evenList.append(num)

	

	return isEven2(num+1)
print(isEven2(0))




def countvouv(mystring):
	list2 = []
	if len(mystring) == 0:
		return 
	elif mystring[0] == 'a' or mystring[0] == 'e' or mystring[0] == 'i' or mystring[0] == 'o' or mystring[0] == 'u':
		#return 1 + countvouv(mystring[1:])
		print(mystring[0])

	return countvouv(mystring[1:])
		
	
#countvouv('ahojiu')
def countnotvouv(mystring):
	if len(mystring) == 0:
		return 
	elif mystring[0] == 'a' or mystring[0] == 'e' or mystring[0] == 'i' or mystring[0] == 'o' or mystring[0] == 'u':
		#return 1 + countvouv(mystring[1:])
		countnotvouv(mystring[1:])
	else:
		print(mystring[0])
		countnotvouv(mystring[1:])
	
	#return countnotvouv(mystring[1:])

countnotvouv('ahojjjsa')


def myReverse(myList):
	newList = []
	for i in range(len(myList)):
		newList.append(myList.pop())
	return newList

print(myReverse([1,2,3,4,5]))