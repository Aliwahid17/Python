# this code solve armstrong number problem by creating a function and it return true and false
def is_armstrong_number(number):
    numberstr = str(number)
    length = len(numberstr)
    num = number
    rev = 0
    temp = 0
    while num != 0:
        rem = num % 10
        num //=  10
        temp += rem ** length
    return temp == number

is_armstrong_number(5)
