#INPUT SAMPLE: The first argument is a file that contains multiple sentences, one per line. Empty lines are also possible.
import os


def reverseSentence(path):
    with open(path) as file:
        for line in file:
            new_sentence = line.rstrip('\r\n')
            new_sentence = new_sentence.split(" ")
            print " ".join(new_sentence[::-1])

reverseSentence("/Users/Dias/Desktop/teste.txt")




