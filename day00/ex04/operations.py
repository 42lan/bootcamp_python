import sys


def usage():
    print("Usage: python operations.py")
    print("Example:")
    print("\tpython operations.py 10 3")


def error_input():
    print("InputError: only numbers\n")
    usage()


def error_many_argv():
    print("InputError: too many arguments\n")
    usage()


def elementary_math(a, b):
    print("Sum:\t\t", a + b)
    print("Difference:\t", a - b)
    print("Product:\t", a * b)
    print("Quotient:\t", "ERROR (dib by zero)" if b == 0 else str(a / b))
    print("Remainder:\t", "ERROR (modulo by zero)" if b == 0 else str(a % b))


def main():
    """
    This program that prints the results of the four elementary mathematical
    operations of arithmetic (addition, subtraction,)multiplication, division)
    and the modulo operation.
    """
    if len(sys.argv) > 3:
        error_many_argv()
    elif len(sys.argv) == 3:
        if sys.argv[1].isdigit() and sys.argv[2].isdigit():
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            elementary_math(a, b)
        else:
            error_input()
    else:
        usage()


if __name__ == '__main__':
    main()
