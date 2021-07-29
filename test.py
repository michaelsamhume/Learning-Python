import sys

def compare(x, y, z):
    if(x<y) and (x<z):
        print("x is least")
    elif(y<z):
        print("y is least")
    else:
        print("z is least")
