#INPUT SAMPLE: The first argument will be a path to a filename containing positive integers, one per line.

def fileReader(path):
    with open(path) as file:
        for line in file:
            sumDigits(line)

def sumDigits(number):
    sum_number = 0
    number = int(number)
    while number != 0:
        sum_number += number%10
        number/=10
    print sum_number

fileReader("/Users/Dias/Desktop/test.txt")
