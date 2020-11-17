#Lukas Rasocha (lukr@itu.dk)
#Highest measured = 1601.7
from collections import Counter   


def search_pascal_multiples_fast(row_limit): 
    old = [1,4,6] # I decided to start from the 5th row, because it is the first row that will count something (after excluding the first and last 2 elements)
                  # I also decided to create only half of the triangle, because the other half is 'the mirror' of the first half 
                  # (so eventually I can just multiply the occurence of numbers in one row by 2 (when the number of elements in the row is even))
                  # and multiply the occurence of numbers in one row by 2 apart from the number in the middle of the row (when the number of elements in the row is odd)
    odd = []
    even = []
    for i in range(4,row_limit):
        if i%2 ==0:
            new = [1,old[1]+1] + [old[i] + old[i+1] for i in range(1,len(old)-1)] # for rows with even number of elemenets
            even = even + new[2:] # excluding the first two elements 
        else:
            new = [1,old[1]+1] + [old[i] + old[i+1] for i in range(1,len(old)-1)] + [old[-1]*2] # for rows with odd number of elements
            odd = odd + new[2:-1] #again exluding the first two elements plus exluding the middle element of a row with odd number of elemenets
        old = new  #updating to be able to calculate the next row
    huge = even + odd
    counter = Counter(huge)
    final = []
    for key,value in counter.items():
        if value*2 > 3: #since I created only half of the triangle I multiply the number of occurence by 2 and check if it appears more than 3 times
            final.append(key)
    final.sort()
    return final

#----------- DO NOT CHANGE ANYTHING BELOW THIS LINE


def search_pascal_multiples_slow(row_limit):

    # Building up Pascal's triangle with a dict of lists
    ptriangle = {}
    ptriangle[0] = [1]
    ptriangle[1] = [1,1]
    ptriangle[2] = [1,2,1]
    for r in range(3, row_limit):
        ptriangle[r] = []
        for i in range(len(ptriangle[r-1])+1):
            if i == 0: # on left border, so we just add 1
                ptriangle[r].append(1)
            elif i == len(ptriangle[r-1]): # on right border, so we just add 1
                ptriangle[r].append(1)
            else: # not on border, so we sum up the two numbers above
                ptriangle[r].append(ptriangle[r-1][i-1] + ptriangle[r-1][i])

    # Putting all numbers into one list, except the outermost 2 numbers in each row
    number_list = []
    for r in range(row_limit):
        row = ptriangle[r]
        for i, number in enumerate(row):
            if i > 1 and i < len(row)-1: # exclude the outermost 2 numbers in each row
                number_list.append(number)

    # Counting the numbers
    number_set = set(number_list) 
    pascal_multiples = []
    for unique_number in number_set:
        count = 0
        for number in number_list:
            if number == unique_number:
                count = count + 1
        if count > 3:
            pascal_multiples.append(unique_number)
    
    return sorted(pascal_multiples)


from timeit import default_timer as timer

def main():
    row_limit = 250
    start = timer()
    print(search_pascal_multiples_slow(row_limit))
    end = timer()
    runtime_slow = end-start
    start = timer()
    print(search_pascal_multiples_fast(row_limit))
    end = timer()
    runtime_fast = end-start
    print(round(runtime_slow / runtime_fast, 2))

if __name__ == "__main__":
    main()