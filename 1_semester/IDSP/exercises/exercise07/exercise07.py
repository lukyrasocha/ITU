#Write a function that will take a string as input and return a swapped case version.
# This Is Interesting 
# tHIS iS iNTERESTING

def swapCase(myString):
	newString = ""
	for i in myString:
		if i.islower():
			newString = newString + i.capitalize()
		else:
			newString = newString + i.lower()
	return newString


#Write a function that will take a string as input and return a version stripped of trailing whitespace.

def myStrip(myString):
	x = list(myString)
	# for i in range(len(x)):
	# 	if x[len]
	while x[-1] == " ":
		x.pop()

	finalWord = ""
	for letter in x:
		finalWord = finalWord + letter
	return finalWord


#Write a function that will take a string as input and return a version where all instances of the letter ‘a’ are replaced with ‘4’.

def myReplace(myString):
	x = list(myString)
	for i in range(len(x)):
		if x[i] == "a":
			x[i] = "4"

	newSentence = ""
	for letter in x:
		newSentence += letter
	return newSentence


#Write a function that will take a string as input and return a version where all alphabetical characters are replaced with ‘*’.

def myReplace2(myString):
	x = list(myString)
	for i in range(len(x)):
		if x[i].isalpha():
			x[i] = "*"

	newSentence = ""
	for letter in x:
		newSentence += letter
	return newSentence



# Write a function that takes in an integer n ≥ 1000 and returns a
# string using the number in a sentence. The number should be
# formatted such that it uses a comma as a thousand separator

def myFormat():
	number = 1002
	if int(number) >= 1000:
		print(f"I wish I had ${number:,}".format(number))


# Write a function that takes two strings, name and country, as input
# parameters and returns a string using them both in a sentence. Use
# a string method to ensure that both input strings will be in title case.

def nameCountry(name,country):
	name = name.title()
	country = country.title()
	print("My name is {0} and I am from {1}".format(name,country))


def readinFile(file):
	myFile = open(file, "r")
	allLines = myFile.read()
	myList = allLines.split("\n")
	# myList = []
	# for line in myFile:
	# 	myList.append(line)
	myFile.close()
	return myList

# Using the open() method, write a function that will take a list as input and
# return a .txt file with only the items that don’t contain digits.
# Each item should be written in lowercase and take up one line in the file.
# Use this function to write out a new file based on the list you created from
# wordList.txt.

def writeinFile(myList):
	f = open("newFile.txt", "w")

	for word in myList:
		if not any(char.isdigit() for char in word):
			f.write(word.lower() + "\n")

	f.close()
	return f

# Write a function that will take a string as input and return the
# number of occurrences of the pattern ‘a9’.

import re

def countPattern(myString):
	pattern = "a9"
	listOfOccurences = re.findall(pattern, myString)

	return print(len(listOfOccurences))


# ) Write a function that will take a string as input and return True if the
# string is formatted as an email address.

def isEmail(email):
	regex = '^[a-z0-9.]+@+[a-z]+[.]+[a-z]{2,3}+$'
	if re.search(regex, email):
		print("VALID EMAIL")
	else:
		print("NOT VALID EMAIL")

def main():
	print(swapCase("Tohle JE mUJ tEsT"))
	print(myStrip("This sentence has spaces at the end        "))
	print(myReplace("This aaa sentence has many a's"))
	print(myReplace2("This test sentence 5523 lol"))
	myFormat()
	nameCountry("LuKas", "ireLand")
	print(readinFile("wordList.txt"))
	writeinFile(readinFile("wordList.txt"))
	countPattern("Ghlja9d$sj9ahHA9hsna987dAa")
	email = 'rasocha.lukas@gmail.com'
	email2 = 'luky1323@gmail.com'
	email3 = '@lukas.cz'
	email4 = 'h824sd@seznam.cz'
	email5 = 'sdassadads.com'
	email6 = '3253sdmadSD@dsad'
	isEmail(email)
	isEmail(email2)
	isEmail(email3)
	isEmail(email4)
	isEmail(email5)
	isEmail(email6)

	

main()