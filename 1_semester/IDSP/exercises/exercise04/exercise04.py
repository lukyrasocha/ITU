#ex 1

numbers = [1,2,3,4,5,6,7,8,9]

# def countEven(myList):
# 	if len(myList) > 2:
# 		if myList[0]%2 == 0:
# 			myList.pop(0)
# 			return 1 + countEven(myList[1:])

# 		elif myList[0]%2 != 0:
# 			myList.pop(0)
# 			return 0 + countEven(myList[1:])

# 		elif myList == []:
# 			return 0
# 		else:
# 			return 0

# print(countEven(numbers))

def isEven(numbers, index, c):
	if index == len(numbers):
		return c
	if numbers[index] % 2 == 0:
		c = c + 1

	return isEven(numbers, index + 1, c)

print(isEven(numbers,0,0))

def isEven2(myList, count):
	if len(myList) == 0:
		return count
	if myList[0] % 2 == 0:
		count = count + 1
	return isEven2(myList[1:], count)

print(isEven2(numbers, 0))

def isEven3(myList):
	if len(myList) == 0:
		return 0
	if myList[0] % 2 == 0:
		return 1 + isEven3(myList[1:])
	else:
		return 0 + isEven3(myList[1:])

print("This is the right one", isEven3(numbers))


#ex 2

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12] ]

def printType(myList):
	if len(myList) == 0:
		return
	else:
		print(myList[0], ":", type(myList[0]))
		return printType(myList[1:])

printType(datalist)


#ex 3

def printNumbers(x=0):
	if x !=3 and x != 5:
		print(x)
	if x <= 5:
		printNumbers(x+1)
	else:
		return

printNumbers()

#ex 4
longList = list(range(100,401))

# def checkDigits(longList):
# 	x = str(longList[0])
# 	y = list(x)
# 	if y[0]%2 == 0:

def checkDigits(longList):
	finalList = []
	for i in range(len(longList)):
		count = 0
		string = str(longList[i])
		l = list(string)
		for k in l:
			c = int(k)
			if c%2 == 0:
				count = count + 1
			else:
				break
		if count == len(l):
			finalList.append(longList[i])
			

	return finalList

print(checkDigits(longList)) 


#90-100:A, 80-89:B, 70-79:C, 60-69:0, <60:F

def grade(grade):
	if grade <=100 and grade >= 90:
		print("The grade is A") 
	
	elif grade <=89 and grade >= 80:
		print("The grade is B") 
	elif grade <=79 and grade >= 70:
		print("The grade is C")
	elif grade <=69 and grade >= 60:
		print("The grade is D")  
	elif grade < 60:
		print("The grade is F")
	else:
		print("You need to put a grade in range 0-100")

def isleap(year):
	if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		print("Year is a leap year")
	else:
		print("year is not a leap year")

# True and True
# -> True

# False and True
# -> False

# 1 == 1 and 2 == 1
# -> False


# "test" == test
# -> False


# 1 == 1 or 2 != 1
# -> true

# False and 0 != 0
# -> False


# "test" == "testing"
# -> True

# 1 != 0 and 2 == 1
# -> False

# not (1 != 10 or 3 == 4)
# -> False

# 1 == 1 and not ("testing" == 1 or 1 == 0)
# -> True

# "chunky" == "bacon" and not (3 == 4 or 3 == 3)
# -> False

# 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
# -> False

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

print(factorial(5))

def strlen(mystring):
	if len(mystring) == 0:
		return 0
	else:
		return 1 + strlen(mystring[1:])

print(strlen("ahojjjj"))


def countvouv(mystring):
	list2 = []
	if len(mystring) == 0:
		return 
	elif mystring[0] == 'a' or mystring[0] == 'e' or mystring[0] == 'i' or mystring[0] == 'o' or mystring[0] == 'u':
		#return 1 + countvouv(mystring[1:])
		print(mystring[0])
	
	return countvouv(mystring[1:])
		
	
	print(countvouv('ahojiu'))
def countnotvouv(mystring):
	if len(mystring) == 0:
		return 
	elif mystring[0] == 'a' or mystring[0] == 'e' or mystring[0] == 'i' or mystring[0] == 'o' or mystring[0] == 'u':
		#return 1 + countvouv(mystring[1:])
		return countvouv(mystring[1:])
	else:
		print(mystring[0])
	
	return countvouv(mystring[1:])

countvouv('ahoj')
countnotvouv('ahoj')

def ispalendrime(mystring):
	if len(mystring) == 0:
		return ""
	
	reverse = ispalendrime(mystring[1:]) + mystring[0]
	if mystring == reverse:
		print("Yes it is palendrime")
	else:
		print("no")
	return reverse
	
print(ispalendrime('racecar'))

