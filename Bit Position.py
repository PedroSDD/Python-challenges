# Given a number n and two integers p1,p2 determine if the bits in position p1 and p2 are the same or not.
# Positions p1 and p2 are 1 based.

def checkFirstBit(n, p1, p2):
    if bin(n)[p1] == bin(p2)[p2]:
        print True
    else:
        print False


#checkFirstBit(86, 2, 3)----->True
#checkFirstBit(125,1,2)------>False
