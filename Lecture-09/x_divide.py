#Example of common exceptions
try:
    print("start of program")
    x = 1 / 0 #ZeroDivisionError
    print(f"x = {x}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
    
print("End of Program")