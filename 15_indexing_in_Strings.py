# indexing = accessing elements of a sequence using [] (indexing operator)
# [start: end: step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # 1
print(credit_number[1]) # 2
print(credit_number[2]) # 3
print(credit_number[3]) # 4
print(credit_number[4]) # -
# using only one value in [] -> [start] not end, step

print(credit_number[0:4]) # 1234
print(credit_number[0:5]) # 1234- 

# starting index is inclusive অন্তর্ভুক্তিমূলক (with that starting index)
# ending index is exclusive (without the ending index, but before it) 

print(credit_number[:8]) # if we dont give the starting index, python thinks it as the starting 0 index by default
# 1234-567
print(credit_number[5:9]) # 5678

print(credit_number[5:]) #if we dont give the ending index but use the ':' after starting index, then it will give us all from the starting index to end of that string or sequence
# 5678-9012-3456

# if we use -value, negative value then it will be the index from the end to righ side direction
print(credit_number[-1]) # 6
print(credit_number[-2]) # 5
print(credit_number[-3]) # 4

# credit_number = "1234-5678-9012-3456"
#                  1 3 - 6 8 9 1 - 4 6
#step
# if var[::2] then python assume that from the stat and till the end, every 2th value , 1st one then after the 2nd one of the string
print(credit_number[::2]) #13-6891-46
print(credit_number[::3]) #146-136

# credit_number = "1234-5678-9012-3456"
# a program to get the last 4 digit of a credit card nuber
last4Digits = credit_number[-4:] #from the -4 to the end
print(f"XXXX-XXXX-XXXX-{last4Digits}") #XXXX-XXXX-XXXX-3456


# reverse a string!
res = credit_number[::-1] # [::-1] this will reverse a string
print(f"Reversed credit card number: {res}") #Reversed credit card number: 6543-2109-8765-4321