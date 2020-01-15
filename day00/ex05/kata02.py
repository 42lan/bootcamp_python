def add_zero(date):
    i = 0
    items = date.split(" ")
    while i < len(items):
        if len(items[i]) == 1:
            items[i] = "0" + items[i]
        i += 1
    return items


def prepare_data(raw_date):
    i = 0
    data = ""
    length = len(raw_date)
    while i < length:
        data += str(raw_date[i])
        if i < length - 1:
            data += " "
        i += 1
    return data


def add_format(date):
    i = 0
    length = len(date)
    formatted_data = ""
    while i < length:
        formatted_data += date[i]
        if i < 2:
            j = '/'
        elif i == 2:
            j = ' '
        elif i > 2:
            j = ':'
        if i < length - 1:
            formatted_data += j
        i += 1
    return formatted_data


def format_data(raw_date):
    return add_format(add_zero(prepare_data(raw_date)))


def print_formatted_date(raw_data):
    formatted_data = format_data(raw_data)
    print(formatted_data)


def main():
    t = (3, 30, 2019, 9, 25)
    print_formatted_date(t)


if __name__ == '__main__':
    main()
