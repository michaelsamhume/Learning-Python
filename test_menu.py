def add(x,y):
    print(x+y)
    menu()
    return x+y

def sub(x,y):
    return x-y

def menu():
    option =input('1) add, 2) subtract')
    x = input('Pick first number')
    x = int(x)
    y = input('Pick second number')
    y = int(y)
    if int(option)==1:
        print(add(x,y))
    if int(option)==2:
        print(sub(x,y))

if __name__=='__main__':
    menu()
