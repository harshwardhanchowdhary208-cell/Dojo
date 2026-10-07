# Question: Solve the given array/string challenge using the required logic.
# Add your solution here.

def compress_string(s):
    # Handle empty string edge case
    if not s:
        return s
        
    compressed = []
    current_char = s[0]
    count = 1
    
    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            # Append the character and its consecutive count
            compressed.append(current_char + str(count))
            current_char = s[i]
            count = 1
            
    # Append the last character group
    compressed.append(current_char + str(count))
    
    # Join the list into a single compressed string
    compressed_str = "".join(compressed)
    
    # Return compressed string only if it is strictly shorter than the original
    if len(compressed_str) < len(s):
        return compressed_str
    else:
        return s
input_string = input()   
result = compress_string(input_string)
print(result)
