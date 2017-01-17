def conditional_multiplication(a_condition, number):
    if a_condition is True:
        return (number * 10)
    else:
        return number

if __name__ == '__main__':
    print(conditional_multiplication(False, 10))
