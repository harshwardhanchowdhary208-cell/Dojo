# Question: What problem does this code solve?
# Find the common elements between two sorted arrays.


def find_intersection(arr1, arr2):
    i, j = 0, 0
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

    return result


if __name__ == "__main__":
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    result = find_intersection(arr1, arr2)
    if not result:
        print(-1)
    else:
        print(*result)
