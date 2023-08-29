#!/usr/bin/python3
def safe_print_division(a, b):
    x = -1
    try:
        x = (a / b)

    except (TypeError, ZeroDivisionError):
        return (None)
    finally:
        if (x == -1):
            x = None
        print("inside result: {}". format(x))
        return (x)
