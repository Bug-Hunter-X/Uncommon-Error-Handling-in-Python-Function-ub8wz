def function_with_uncommon_bug(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

print(function_with_uncommon_bug(0))
print(function_with_uncommon_bug(2))
print(function_with_uncommon_bug('a'))

#Uncommon Bug:
#The function fails to handle the case where x is a string that can be converted to a number such as '2'.
#This results in a TypeError, which is caught but does not allow for the intended behavior. 