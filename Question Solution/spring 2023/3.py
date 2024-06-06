# number  = 22
# div = 0
# result  = number/div
# print(result)


number  = 22
div = 0
try:
    result  = number/div
except ZeroDivisionError:
    print("a number can't be divided by zero")
else:
    print(result)