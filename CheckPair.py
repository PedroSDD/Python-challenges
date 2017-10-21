#INPUT SAMPLE: Your program should accept as its first argument a filename.
# This file will contain a comma separated list of sorted numbers and then the sum 'X', separated by semicolon.
#Ignore all empty lines. If no pair exists, print the string NULL

import itertools

def fileReader(path):
    with open(path) as file:
        for line in file:
            checkPair(line)

def checkPair(line):
    line = line.strip().split(";")
    column_value = line[-1]
    line = line[:-1]



def pairMaker(line, column_value):
    for i in line:


fileReader("/Users/Dias/Desktop/test.txt")