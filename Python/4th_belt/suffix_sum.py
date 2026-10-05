# Python3 code to demonstrate
# Suffix List Sum
# using list comprehension + sum() + list slicing

# initializing list
test_list = [3, 4, 1, 7, 9, 1]

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + sum() + list slicing
# Suffix List Sum
test_list.reverse()
res = [sum(test_list[: i + 1]) for i in range(len(test_list))]

# print result
print("The suffix sum list is : " + str(res))

# or

def suffix_sum(lst):
    result = []
    sum = 0
    for i in range(len(lst) - 1, -1, -1):
        sum += lst[i]
        result.append(sum)
    return result


  # input sample list
test_list = [3, 4, 1, 7, 9, 1]
print("The original list :", test_list)

res = suffix_sum(test_list)

# printing list 
print("The suffix sum list is :", res)

# or

def suffix_sum_recursive(lst, sum=0, result=None):
    if result is None:
        result = []
    if len(lst) == 0:
        return result
    sum += lst[-1]
    result.append(sum)
    return suffix_sum_recursive(lst[:-1], sum, result)


# input sample list
test_list = [3, 4, 1, 7, 9, 1]
print("The original list :", test_list)

res = suffix_sum_recursive(test_list)

# printing the list
print("The suffix sum list is :", res)

# or

from itertools import accumulate

test_list = [3, 4, 1, 7, 9, 1]

# printing original list
print("The original list : " + str(test_list))

suffix_sum = list(accumulate(reversed(test_list)))

# printing the list
print("The suffix sum list is:", suffix_sum)

# or

def suffix_sum_generator(lst):
  
    suffix_sum = []
    suffix_sum_gen = (sum(lst[i:]) for i in range(len(lst)))
    for num in reversed(list(suffix_sum_gen)):
        suffix_sum.append(num)
    return suffix_sum


# Sample input
test_list = [3, 4, 1, 7, 9, 1]
print("The original list :", test_list)

# Call suffix_sum_generator() function
res = suffix_sum_generator(test_list)

# printing list
print("The suffix sum list is :", res)

# or

# import numpy library
import numpy as np

# initialize list
test_list = [3, 4, 1, 7, 9, 1]

# reverse the list using slicing and compute the cumulative sum using numpy.cumsum()
# then reverse the result again to obtain the correct order of suffix sum values
suffix_sum = np.cumsum(test_list[::-1])[::-1].tolist()

# create a list of indices in descending order
index_list = list(range(len(test_list)-1, -1, -1))

# use the index list to access the suffix sum values in the correct order
suffix_sum_ordered = [suffix_sum[i] for i in index_list]

# print the ordered suffix sum list and the index list
print("Index list:", index_list)
print("Ordered suffix sum list:", suffix_sum_ordered)# import numpy library
import numpy as np

# initialize list
test_list = [3, 4, 1, 7, 9, 1]

# reverse the list using slicing and compute the cumulative sum using numpy.cumsum()
# then reverse the result again to obtain the correct order of suffix sum values
suffix_sum = np.cumsum(test_list[::-1])[::-1].tolist()

# create a list of indices in descending order
index_list = list(range(len(test_list)-1, -1, -1))

# use the index list to access the suffix sum values in the correct order
suffix_sum_ordered = [suffix_sum[i] for i in index_list]

# print the ordered suffix sum list and the index list
print("Index list:", index_list)
print("Ordered suffix sum list:", suffix_sum_ordered)