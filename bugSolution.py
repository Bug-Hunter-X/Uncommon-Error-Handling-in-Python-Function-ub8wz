def function_with_uncommon_bug_solution(x):
    try:
        x = float(x)
        result = 10 / x
        return result
    except ValueError:
        return "Invalid input: Cannot convert to number"
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

print(function_with_uncommon_bug_solution(0))
print(function_with_uncommon_bug_solution(2))
print(function_with_uncommon_bug_solution('a'))
print(function_with_uncommon_bug_solution('2'))