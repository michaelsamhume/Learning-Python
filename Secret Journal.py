def check_password(test):
    if test == 'foo':
        print('Hello Michael')
        return True
    else:
        print('Bad password')
        return False


pwd = input('Pick a password.\n')
if len(pwd)>8:
    good = check_password(pwd)
else:
    good = False
    print('Password too short.')
print('Password is good:' +str(good))