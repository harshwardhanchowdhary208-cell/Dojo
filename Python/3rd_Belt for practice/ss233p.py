# Question: Solve the given array/string challenge using the required logic.
# Add your solution here.

def compress_string(s):
    if not s:
        return s
    compress = []
    current_char=s[0]
    count=1
    for i in s:
        if s[i]==current_char:
            count+=1
        else:
            compress.append(compress + str(count))
            current_char=s[i]
            count=1
    compress.append(compress + str(count))
    compress_str="".join(compress)
    if len(compress_string) < len(s):
        return compress_string
    else:
        return s
a=input()
b=compress_string(a)
print(b)
