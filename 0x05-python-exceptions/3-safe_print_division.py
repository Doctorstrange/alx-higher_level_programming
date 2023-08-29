#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        x = (a / b)

    except (TypeError, ZeroDivisionError):
        x = None
    finally:
        print("inside result: {}". format(x))
        return (x)
