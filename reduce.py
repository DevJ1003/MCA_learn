from functools import reduce

sequences = [10,2,8,7,5,4,3,11,1]
filtered_result = reduce(lambda x,y:x*y, sequences)
print(filtered_result)