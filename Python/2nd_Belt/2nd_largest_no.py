# Question: What problem does this code solve?
# Add your solution here.

n = int(input())
arr = list(map(int, input().split()))
unique_elements = set(arr)
sorted_li = list(unique_elements)
sorted_li.sort()
if len(sorted_li) == 1:
    print("-1")
else:
    print(sorted_li[-2])