def display_right_format(string):
    length = len(string)
    if length < 42:
        nb = 42 - length
        while nb > 0:
            print("-", end="")
            nb -= 1
        print(string, end="")
    else:
        print(string[:42], end="")


def main():
    phrase = "The right format"
    display_right_format(phrase)


if __name__ == '__main__':
    main()
