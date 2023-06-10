def wrapper(f):
    def fun(l):
        standardized_numbers = []
        for number in l:
            if len(number) == 10:
                standardized_number = '+91 ' + number[:5] + ' ' + number[5:]
            elif len(number) == 11:
                standardized_number = '+91 ' + number[1:6] + ' ' + number[6:]
            elif len(number) == 12:
                standardized_number = '+91 ' + number[2:7] + ' ' + number[7:]
            else:
                standardized_number = number
            standardized_numbers.append(standardized_number)
        return f(standardized_numbers)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
