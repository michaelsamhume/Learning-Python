import sys

def compare(x, y, z):
    if(x<y) and (x<z):
        print("x is least")
    elif(y<z):
        print("y is least")
    else:
        print("z is least")

if __name__ == "__main__":
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    x=sys.argv[1]
    y=sys.argv[2]
    z=sys.argv[3]
    compare(x,y,z)