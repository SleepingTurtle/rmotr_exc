def make_number_odd(number):
    if (number % 2 == 0):
        return number + 1
    else:
        return number

if __name__ == '__main__':
    print(make_number_odd(3))
