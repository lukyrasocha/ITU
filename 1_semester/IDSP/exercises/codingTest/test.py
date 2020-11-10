
nums = [-99,45,8,45,8,5,6,6]

def compute_mode(myList):
	counter_list = []
	for i in myList:
		counter = 0
		for j in myList:
			if i == j:
				counter += 1
		counter_list.append(counter)

	maxValue = max(counter_list)
	newList = []

	indices = [i for i, x in enumerate(counter_list) if x == maxValue]

	for i in indices:
		if myList[i] not in newList:
			newList.append(myList[i])
	newList.sort()
	
	return newList

print(compute_mode(nums))























# def read_file(filename):
# 	infile = open(filename, 'r')
# 	x = infile.readlines()
# 	newList = []
# 	for line in x:
# 		x = line.split('\n')
# 		x.pop()
# 		newList.append(x)
# 	#print(newList)
# 	finalList = []
# 	for i in newList:
# 		for j in i:
# 			finalList.append(j.split(','))
# 	#print(finalList)

# 	dictionary = {}
# 	headers = finalList[0]
# 	for header in headers:
# 		dictionary[header] = []

# 	for header in headers:
# 		for i in finalList[1:]:
# 			dictionary[header].append(i[headers.index(header)])

# 	return dictionary
	# print(dictionary)
	# print(dictionary['Header1'])
	# for i in finalList:
	# 	for j in i:
	# 		print(j)

def read_csv(filename):
	with open(filename, 'r') as f:
		newList = []
		for row in f:
			newList.append(row.strip().split(','))
		print(newList)

	dictionary = {}
	headers = newList[0]

	for header in headers:
		dictionary[header] = []

	for header in headers:
		for i in newList[1:]:
			dictionary[header].append(i[headers.index(header)])

	return dictionary
print(read_csv('test.csv'))



def read_csv(filename):
	infile = open(filename, 'r')
	x = infile.readlines()
	newList = []
	for line in x:
		x = line.split('\n')
		x.pop()
		newList.append(x)
	infile.close()
	#print(newList)
	finalList = []
	for i in newList:
		for j in i:
			finalList.append(j.split(','))
	#print(finalList)

	dictionary = {}
	headers = finalList[0]
	for header in headers:
		dictionary[header] = []

	for header in headers:
		for i in finalList[1:]:
			dictionary[header].append(i[headers.index(header)])

	return dictionary