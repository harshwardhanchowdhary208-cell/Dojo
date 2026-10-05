def find_largest_index(arr):
    if not arr:
        return -1  # Return -1 if array is empty
        
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_index]:
            max_index = i
            
    return max_index

input_array = [10, 25, 7, 31, 18]
output = find_largest_index(input_array)
print("Output:", output)
