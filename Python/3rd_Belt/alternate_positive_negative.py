# Question: Arrange the numbers so positive and negative values alternate in order.
# Add your solution here.

def rearrange(arr):
    # Separate positive (including 0) and negative numbers
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    
    # If all elements belong to only one category, preserve original order
    if not pos or not neg:
        return arr
        
    result = []
    i, j = 0, 0
    
    # Alternate between positive and negative numbers
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1
        
    # Append any remaining elements to the end
    if i < len(pos):
        result.extend(pos[i:])
    if j < len(neg):
        result.extend(neg[j:])
        
    return result
