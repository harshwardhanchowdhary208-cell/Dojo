# Question: Find the index of the largest number in the list.
# Add your solution here.

arr = list(map(int, input().split()))
lar_no = arr[0]
for i in range(0,len(arr)):
  if arr[i] > lar_no:
    lar_no = arr[i]
print(arr.index(lar_no))