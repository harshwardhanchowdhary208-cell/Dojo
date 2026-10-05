# Question: What problem does this code solve?
# Add your solution here.

def find_intersection(arr1, arr2):
    i, j = 0, 1 
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
            
    if not result:
        print(-1)
    else:
        print(*(result))
