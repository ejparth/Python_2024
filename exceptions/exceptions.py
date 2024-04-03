x = (input('Enter no 1 : '))
y = (input('Enter no 2 : '))

try:
    division = int(x) / int(y)
    print("addition is :", division)

except ZeroDivisionError as e:
    print("Error : ", e)
    division = None
    print("Division is : ", division)

except ValueError as e:
    print("Error : ", e)
    division = None
    print("Division is : ", division)

except Exception as e:
    division = None
    print("Enter the numbers again as the problem is : ", e)  ## print the exception
    print("type of exception is ", type(e).__name__)  ##tells the type of exception
