# Question: Use the sliding window technique to solve the array problem.
# Add your solution here.

n = int(input())
arr = list(map(int, input().split()))
t = int(input())

left = 0
current_sum = 0
min_length = float('inf')

for right in range(n):
    current_sum += arr[right]
    
    while current_sum >= t:
        min_length = min(min_length, right - left + 1)
        current_sum -= arr[left]
        left += 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)
