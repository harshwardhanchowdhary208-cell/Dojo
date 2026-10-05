x=input()
if x in'QWERTYUIOPASDFGHJKLZXCVBNM':
    print("Upper case")
elif x in 'qwertyuiopasdfghjklzxcvbnm':
    print('Lower case')
elif x in '1234567890':
    print('Digit')
else:
    print("Special case")