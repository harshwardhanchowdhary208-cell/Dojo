# Question: What problem does this code solve?
# Add your solution here.

a = [3, 4, 1, 7, 9, 1]

res = [] 
cur_s= 0 # current sum

for num in a:
    cur_s += num
    res.append(cur_s)
print(res)

# or

import numpy as np
a = [3, 4, 1, 7, 9, 1]

res = np.cumsum(a)
print(res)

# or

import itertools
a = [3, 4, 1, 7, 9, 1]

res = list(itertools.accumulate(a))
print(res)

# or

a = [3, 4, 1, 7, 9, 1]
res = [sum(a[:i+1]) for i in range(len(a))]

print(res)