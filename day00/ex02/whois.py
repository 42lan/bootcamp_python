import sys


def whois(number):
    if number == 0:
        print("I'm Zero.")
    else:
        print(("I'm Odd", "I'm Even")[(number % 2) == 0])


def main():
    if len(sys.argv) == 1:
        exit()
    elif len(sys.argv) > 2 or not sys.argv[1].isdigit():
        print("ERROR")
    if sys.argv[1].isdigit():
        whois(int(sys.argv[1]))


if __name__ == '__main__':
    main()
