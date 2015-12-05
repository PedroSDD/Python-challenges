# Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not.
# Positions p1 and p2 are 1 based.

def checkFirstBit(n, p1, p2):
    if bin(n)[2] and bin(p1)[2] and bin(p2)[2] == '1':
        print "True"
    else:
        print "False"


checkFirstBit(1, 1, 1)