import sys


def string_from_args():
    x = 1
    string = ''
    while x < len(sys.argv):
        string += sys.argv[x]
        x += 1
        if x < len(sys.argv):
            string += ' '
    return string


def rev_alpha():
    return (string_from_args().swapcase())[::-1]


def main():
    print(rev_alpha())


if __name__ == '__main__':
    main()
