import sys


def whois():
    if len(sys.argv) == 1:
        exit()
    elif len(sys.argv) > 2 or not sys.argv[1].isdigit():
        print("ERROR")
    elif sys.argv[1].isdigit():
        number = int(sys.argv[1])
        if number == 0:
            print("I'm Zero.")
        else:
            if (number % 2) == 0:
                print("I'm Even")
            else:
                print("I'm Odd")


def main():
    whois()


if __name__ == '__main__':
    main()
