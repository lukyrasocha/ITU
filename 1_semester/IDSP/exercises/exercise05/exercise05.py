import random
# EX 1

def myLen(myList):
	myLen = 0
	for x in myList:
		myLen = myLen+1

	return myLen

#EX 2

def myMax(myList):
	x = myList[0]
	for i in range(len(myList)):
		if x < myList[i]:
			x = myList[i]
	return x

print(myMax([5,10,10,35,14,24]))

#EX 3

def myReverse(myList):
	c = []
	for i in myList:
	    c.insert(0,i)
	return c

print(myReverse([1,2,3,4]))

#EX 4

def mySum(myList):
	sume = 0
	for x in myList:
		sume = sume + x
	return sume

print(mySum([1,2,3,10]))

#EX 5

def guess():
	x = random.randint(1,9)
	yourGuess = int(input("Enter your guess: "))

	while yourGuess != x:
		yourGuess = int(input("Wrong, enter another guess: "))

	print("Congrats, thats right!")

#guess()

#EX 6

def drawPattern():
	for j in range(1,6):
		print(j*"*")	
	for i in [4,3,2,1]:
		print(i*"*")

drawPattern()


