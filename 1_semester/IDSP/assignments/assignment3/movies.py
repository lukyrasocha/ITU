def read_csv(filename): 
	nodes =[]
	with open(filename) as f:
		for line in f:
			nodes.append(tuple(line.rstrip().split(','))) # puts the ID, name and type into seperate tuples
	return nodes #or edges

def generate_name_map(nodes):
	name_map = {} 	#creates a dictionary
	for i in nodes:
		name_map[i[0]] = i[1] # the ID is the key and the label (name) is the value
	return name_map

def name_edges(edges,name_map):
	name_edges_list = []
	for i in edges:
		name_edges_list.append((name_map[i[0]],name_map[i[1]],i[2])) # edges have the ID's that are connected and name_map is used to lookup the values under the specific ID
	return name_edges_list


def generate_movie_dictionary(name_edges_list):
	movie_dictionary = {i[1]:[] for i in name_edges_list}	# creates a dictionary where the key is the movie name and the values (for now) are empty lists
	for i in name_edges_list:
	 	if i[2] == 'ACTS_IN':	# checks if the third element is 'ACTS_IN' as we want just the actors and not directors
	 		if i[0] not in movie_dictionary[i[1]]: # this is probably redundant, but it makes sure that we don't add duplicates
	 			movie_dictionary[i[1]].append(i[0]) # appends the empty list with the actors that appeared in the movie
	return movie_dictionary


def get_actor_friends(movie_dictionary):
	actor_friends = {}
	for i in movie_dictionary.values(): # i is the list of all the actors that appeared in a certain movie
		for j in i:
			actor_friends[j] = set()	# assigns an empty set to every single actor

	for i in movie_dictionary.values(): # i is the list of all the actors that appeared in a certain movie
		for j in i:						# j is an individual actor
			for k in range(len(i)):
				if k != i.index(j): 	#so he/she doesn't consider himself/herself as a friend
					actor_friends[j].add(i[k]) #adds all the actors that our 'j' actor has worked with (adds all the remaining names from the list 'i' apart from the actor himself)
	return actor_friends


def main():
	nodes = read_csv('nodes.csv')
	edges = read_csv('edges.csv')
	name_map = generate_name_map(nodes)
	name_edges2 = name_edges(edges, name_map)
	movie_dictionary = generate_movie_dictionary(name_edges2)
	actor_friends = get_actor_friends(movie_dictionary)
	

	#Test cases
	#1
	print('--------------------------------------------------------')
	print(edges[0])
	print(nodes[0])
	#2
	print('--------------------------------------------------------')
	print(name_map['345'])
	#3
	print('--------------------------------------------------------')
	print(name_edges2[0])
	#4
	print('--------------------------------------------------------')
	print(movie_dictionary['The Matrix'])
	#5
	print('--------------------------------------------------------')
	print(actor_friends['Keanu Reeves'])

if __name__ == '__main__':
	main()