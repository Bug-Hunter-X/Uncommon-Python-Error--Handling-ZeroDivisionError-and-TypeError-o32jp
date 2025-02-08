def function_with_uncommon_error(a, b):
    try:
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("Invalid input type. Please use numbers.")
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        result = a / b
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

#Example Usage:
print(function_with_uncommon_error(10,2))
print(function_with_uncommon_error(10,0))
print(function_with_uncommon_error(10,"a"))
print(function_with_uncommon_error("a", 10))