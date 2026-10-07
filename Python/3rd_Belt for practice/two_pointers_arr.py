# Question: Use the two-pointer technique to solve the array problem.
# Add your solution here.

def find_union_sorted(arr1, arr2):
    i, j = 0, 0
    first = True

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            value = arr1[i]

            if first:
                print(value, end="")
                first = False
            else:
                print(" " + str(value), end="")

            while i < len(arr1) and arr1[i] == value:
                i += 1

        elif arr2[j] < arr1[i]:
            value = arr2[j]

            if first:
                print(value, end="")
                first = False
            else:
                print(" " + str(value), end="")

            while j < len(arr2) and arr2[j] == value:
                j += 1

        else:
            value = arr1[i]

            if first:
                print(value, end="")
                first = False
            else:
                print(" " + str(value), end="")

            while i < len(arr1) and arr1[i] == value:
                i += 1

            while j < len(arr2) and arr2[j] == value:
                j += 1

    while i < len(arr1):
        value = arr1[i]

        if first:
            print(value, end="")
            first = False
        else:
            print(" " + str(value), end="")

        while i < len(arr1) and arr1[i] == value:
            i += 1

    while j < len(arr2):
        value = arr2[j]

        if first:
            print(value, end="")
            first = False
        else:
            print(" " + str(value), end="")

        while j < len(arr2) and arr2[j] == value:
            j += 1

    print()