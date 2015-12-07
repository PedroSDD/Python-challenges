#INPUT SAMPLE: The first argument will be a path to a filename containing positive integers, one per line.


def SumOfDigits(path):
    with open(path) as file:
        for line in file:
            line = line.strip()
            list_int = map(int,line)
            print reduce(lambda x,y: x + y,list_int)
