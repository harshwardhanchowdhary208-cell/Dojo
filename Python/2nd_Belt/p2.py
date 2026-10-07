# Question: Print Pascal's triangle for the given number of rows.
# Add your solution here.

def pendulumArrangement(arr):
    n = len(arr)

    arr.sort(key=None, reverse=False)

    ans = []

    ans += [arr[0]] 

    right = True

    for i in range(1, n):

        if right:
            ans += [arr[i]]

        else:
            ans.insert(0, arr[i])

        right = not right

    return ans


arr = [14, 6, 19, 21, 12]
ans = pendulumArrangement(arr)

for i in ans:
    print(i, end=" ")
