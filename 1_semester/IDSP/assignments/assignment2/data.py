#IT University of Copenhagen
#IDSP Assignment 2
#author: Lukas Rasocha (lukr@itu.dk)


def read_file(filename):
	inFile = open(filename, 'r')
	data = inFile.read()
	dataList = data.split("\n") #creates a list where the items are the rows (because we are splitting by \n)
	dataList.pop() # this removes the last empty string '' that is created when splitting the data by \n
	inFile.close()
	return dataList

def parse_csv_lines(lines): # this will take the dataList created from read_file and append the dataSet list with lists created by split(",")
	dataSet = []
	for i in lines:
		dataSet.append(i.split(","))
	return dataSet

def parse_delimited_lines(lines, delimiter):
	dataSet = []
	for i in lines:
		dataSet.append(i.split(delimiter))
	return dataSet

def age_difference(dataSet):
	ageDiff = []
	for i in range(len(dataSet)):
		if dataSet[i] != ['']: #catches if there is an empty list
			difference = float(dataSet[i][1]) - float(dataSet[i][-1]) #for each municipility(i) takes the second item (the first year) and substract the last item(the last year)
			difference = round(difference,2)
			ageDiff.append((dataSet[i][0], difference)) #puts the data in a tuple where the first item is the name of the municipility and the second the calculated difference
	print("*******************************************************************")
	print("AGE difference between the first and last year in each municapality")
	print("*******************************************************************")
	print(ageDiff)
	print("********************************************************************")
	return ageDiff

def find_unisex_names(male_names, female_names):
	male_set = set()	# creates an empty set
	female_set = set()	# creates an empty set

	for i in range(len(male_names)): #adds the male names to the set, using two loops bcs of the nested lists (for example [Lukas, Noah] is the i'th item and then Lukas would be the j'th item (index 0))
		for j in range(len(male_names[i])):
			male_set.add(male_names[i][j])

	for i in range(len(female_names)): #same logic as for males
		for j in range(len(female_names[i])):
			female_set.add(female_names[i][j])

	unisex = male_set & female_set # finds the intersection between the two sets. 

	# otherwise I would just compare the 2 lists one item by one item
	# for name in male_names
	# 	compare name with every single name in female_names
	#	when it is a match store the name in a new unisex list
	
	#	I am not sure about the complexity but I think it is O(n) (the time increases linearly)
	#	so I would say that the intersection function on set is more efficient

	return unisex

def build_name_dataset(female_names, male_names, unisex_names):
	nameTracker = [] # keeps a track of the names that already have been added so we don't do duplicates
	all_names = open("all_names.csv", "w")
	for i in unisex_names:		# write every single name on from unisex on a new line to the file "all_names.csv" together with 'U' 
		nameTracker.append(i)
		all_names.write(i+",U"+"\n")

	for i in range(len(male_names)): #again we have nested lists so we need to loop 2 times through them to access the names
		for j in range(len(male_names[i])):
			if male_names[i][j] not in nameTracker:  # checks if the name has not been added yet
				all_names.write(male_names[i][j] +",M" +"\n")
				

	for i in range(len(female_names)):	#same logic as for males
		for j in range(len(female_names[i])):
			if female_names[i][j] not in nameTracker:
				all_names.write(female_names[i][j] +",F" +"\n")
				
	all_names.close()

	dataList = read_file("all_names.csv")
	return parse_csv_lines(dataList) 

def write_sorted_names(names):

	for i in names:
			
			x = open(i[0][0]+".csv","a") # this takes the first letter of the name (because strings are also iterable) (because names are stored under index 0 and their sex under index 1)
									     # "a" stands for "append" and so it does not overwrite what has been previously writte in the file but just appends it of a new thing
			x.write(i[0] + "," + i[1] + "\n")  # after the appropriate file has been opened you write the name (index 0) and and the sex (index 1) into it
			x.close()

	# please note that it takes some time to actually create the 32 files so it "stucks" for a few seconds before it prints "Done"
	print("Done")
	return


def main(): #Here I run the functions with the appropiate csv files
	# Here you will need to call some or all of the above functions to test that your code is working. Some functions will generate an output that is used as input in another function.
	municapalities_data = read_file("municipalities-2005-2019.csv")
	dataSet = parse_delimited_lines(municapalities_data, ";")
	age_difference(dataSet)
	raw_male = read_file("male_names.csv")
	raw_female = read_file("female_names.csv")
	male_names = parse_csv_lines(raw_male)
	female_names = parse_csv_lines(raw_female)
	unisex_names = find_unisex_names(male_names,female_names)
	#write_tuples()
	built_dataset = build_name_dataset(female_names,male_names,unisex_names)
	write_sorted_names(built_dataset)


if __name__ == "__main__":
	# Executes only if run as a script
	main()
