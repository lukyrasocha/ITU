import math
print("hello world")


#Exercise 1 A
# In the function calcInterest I would return the interest because now the function returns type "none" so when in the function
# test when adding in the variable amount we are adding something of type int and something of type "None" which gives a type Error

#Exercise 1 B
# the variable "Interest" is a local variable so its not available for the function test 

#Exercise 1 C
def calcInterest(balance,rate):
	interest = balance * (rate * 0.01)
	print("interest is ", interest)
	return interest

interest = 40
print("interest is ", interest)
calcInterest(1000,5)
print("interest is ", interest)

# The variable interest will be printed out 3 times - two times because we print the variable "interest" two times.
# Once because there is a print function inside our function that is then being called with the new calculated interest
# The output will be 2x times interest 40 and two times the new interest 50


#Exercise 1D

def stringPrint(theString):
	print("got: ", theString)
	theString = "In a kingdom by the sea"
	print("set to: ", theString)

outerString = "it was many years ago"
print("before outer string, :", outerString)
stringPrint(outerString)
print("after outer string, :", outerString)

#It will print:
# before outer string, : it was many years ago
# got: it was many years ago
# set to: In a kingdom by the sea
# after outer string, : it was many years ago

def stringPrint2(theString):
	print("got: ", theString)
	theString = "In a kingdom by the sea"
	print("set to: ", theString)
	return theString

outerString2 = "it was many years ago"
print("before outer string, :", outerString2)
outerString2 = stringPrint2(outerString2)
print("after outer string, :", outerString2)

# Now outerString will actually change to our new String because we reassign it and because the first function returns the new string
# that is then assigned to the variable outerString


#Exercise 2
#factorial
print(math.factorial(5))
#square root
print(math.sqrt(4))
#natural logarithm
print(math.log(math.e))
#logaritmh with a base 10
print(math.log10(100))
#logarithm with a base 2
print(math.log2(16))
#greatest divisor
print(math.gcd(8,4))

#Exercise 3 A

def calculateBmi(height,weight):
	bmi = weight / (height **2)
	return bmi

print("Your BMI is", calculateBmi(1.95, 90))

def calculateThreePeople(h1,m1,h2,m2,h3,m3):
	print("Bmi of the first person is ", calculateBmi(h1,m1))
	print("Bmi of the second person is ", calculateBmi(h2,m2))
	print("Bmi of the third person is ", calculateBmi(h3,m3))



#Exercise 3B

def meanSum(num1,num2,num3):
	sume = num1 + num2 + num3
	mean = sume / 3
	return sume, mean

#Exercise 3C

def digitNumber(num1,num2,num3):
	sume = num1 + num2 + num3
	print("The lenght of that number is", len(str(sume)),"digits")





#Exercise 4A
def calculateArea(radius):
	return math.pi * radius ** 2

#Exercise 4B
def distance(x1,x2,y1,y2):
	return math.sqrt(((x1 - y1) ** 2) + (x2 - y2) ** 2)

#Exercise 4C

def anotherArea(x1,x2,y1,y2):
	return math.pi * (distance(x1,x2,y1,y2) ** 2)


#Exercise 5
r = 6378.1 * 1000
m = 5.9741 * 10 ** (24)
def escapeVelocity(mass, radius):
	g = 6.67 * 10**(-11)
	#ve = math.sqrt((2 * 6.67 * 10**(-11) * mass) / radius*1000)
	ve = (math.sqrt((2*g*mass) / radius))/1000
	return ve

def main():
	calculateThreePeople(1.84,75, 1.93, 81, 1.65, 56)
	sume, mean = meanSum(1,2,3)
	print("The sum is", sume, "The mean is", mean)
	digitNumber(10,5,1)
	print("The area of the circle is", calculateArea(4))
	print("Distance between two points is", distance(0,3,0,-3))
	print("The area of a circle is", anotherArea(15,12,34,12))
	print("The escapeVelocity for the Earth is ", escapeVelocity(m,r), "km/s")
main()



