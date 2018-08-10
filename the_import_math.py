import math
def quadratic(a,b,c):
    x1 = (math.sqrt(b*b-a*c*4)-b)/2*a
    x2 = (-math.sqrt(b*b-a*c*4)-b)/2*a
    return x1,x2