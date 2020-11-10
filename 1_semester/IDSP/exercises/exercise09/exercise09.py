#EX 1

myPet = {}

myPet['name'] = 'Spot'
myPet['animal'] = 'dog'
myPet['age'] = 4
myPet['fave_snacks'] = ['sausages', 'peanut butter', 'dropped popcorn']

print(myPet)


#EX 2

inventory = {
	'gold' : 500,
	'pouch' : ['flint', 'twine', 'gemstone'],
	'backpack' : ['xylophone', 'dagger','bedroll','bread loaf']
}

inventory['pocket'] = ['seashell', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold']+50
print(inventory)

#EX 3

def readFile(file):
	x = open(file, 'r')
	data = x.read()
	myList = data.lower().split("\n")
	myList.remove("")
	return myList

print(readFile("JFK.txt"))

def filter(myList):
	mySet = set(myList)

	return mySet

print(filter(readFile("JFK.txt")))

def count(myList):
	dictionary = {}
	for i in myList:
		count = 0
		for j in range(len(myList)):
			if i == myList[j]:
				count += 1
		dictionary[i] = count
	return dictionary	

print(count(readFile("JFK.txt")))

x = count(readFile("JFK.txt"))
print("The count of the word 'the' is:", x["the"])


#List comprehensions

#EX 9 

list1 = [i for i in range(10)]
print(list1)

list2 = [i**2 for i in list1]
print(list2)

list3 = [i**3 for i in list1 if list1.index(i)%2 != 0]
print(list3)

students = {"dennis": 23, "david": 21, "mary": 9, "daniel":
25, "darius": 17, "jim": 10, "marvin": 19}

students2 = {i.upper():students[i] for i in students}
print(students2)

voting = [i for i in students if students[i] >= 18]
print(voting)