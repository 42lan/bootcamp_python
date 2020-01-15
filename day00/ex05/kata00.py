def kata00(t):
    i = 0
    string = ""
    length = len(t)
    if t is None or length == 0:
        print("The tuple is empty")
        exit()
    while i < length:
        string += str(t[i])
        if i < length - 1:
            string += " "
        i += 1
    print("The", length, "number is:" if length == 1 else "numbers are:", string)


def main():
    t = (1,2,19,42,21)
    kata00(t)


if __name__ == '__main__':
    main()
