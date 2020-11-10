def problem():
	x = input()   #string
	myList = list(x)
	if int(x) >= 10 and int(x) <=1000:
		while len(myList) != 1:
			result = 1
			for i in myList: 
				myDigit = int(i)
				if myDigit != 0:
					result = result * myDigit
					myList = list(str(result))
			print(result)
	return int(myList[0])

print(problem())