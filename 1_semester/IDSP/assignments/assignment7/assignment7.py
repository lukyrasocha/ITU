

# def pascal(rows):
#     """
#     docstring
#     """
#     old = [1,4,6,4,1]
#     for i in range(rows):
#         print(old)
#         #if i%2 ==0:
#         new = [1,old[1]+1] + [old[i] + old[i+1] for i in range(1,len(old)-1)] + [1]
#         #else:
#             #new = [1,old[1]+1] + [old[i] + old[i+1] for i in range(1,len(old)-1)] + [old[-1]*2]
#         old = new  
            


# pascal(10)
from collections import Counter
import numpy as np
def pascal(rows):
    """
    docstring
    """
    old = [1,4,6]
    even = []
    odd = [old]
    hugeList = []
    for i in range(rows):
        #print(old)
        if i%2 ==0:
            new = [1,old[1]+1] + [old[i] + old[i+1] for i in range(1,len(old)-1)]
            #even.append(new)
            hugeList = hugeList + new[2:]*2
        else:
            new = [1,old[1]+1] + [old[i] + old[i+1] for i in range(1,len(old)-1)] + [old[-1]*2]
            #odd.append(new)
            hugeList = hugeList + new[2:-1]*2 + [new[-1]]
        old = new  

    counter = Counter(hugeList)
    # print('EVEN')
    # print(even)
    # print('ODD')
    # print(odd)
    #print('Hugelist is')
    #print(hugeList)
    #print('Counter')
    #print(counter)

    # final = []
    # for key,value in counter.items():
    #     if value > 3:
    #         final.append(key)
    # print('FINAL IS')
    # final.sort()
    # return final
    x = np.array(hugeList)
    key,count = np.unique(x, return_counts=True)
    large = key[count>3]
    print(list(large))


pascal(250)

