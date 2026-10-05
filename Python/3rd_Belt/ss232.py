# Read the full string and the word to remove
S = input()
W = input()

len_S = len(S)
len_W = len(W)
found = False

# Iterate through the string to find the first character match
for i in range(len_S - len_W + 1):
    
    # Check if the substring matches the word W
    if S[i : i + len_W] == W:
        # Reconstruct the string by skipping the matched word
        print(S[:i] + S[i + len_W :])
        found = True
        break
# If the word was not found in the string, print the original string
if not found:
    print(S)
