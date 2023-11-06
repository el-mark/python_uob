a = 5
b = 1

# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
try:
    print(a/b)
    print(int('eee'))
except ZeroDivisionError as err:
    print("you can't divide by zero", err)
except Exception as err:
    print("there was a problem in a/b operation. Err:")
    print(err)
finally:
    print('close algorithm')

print ("thank you, good bye")
