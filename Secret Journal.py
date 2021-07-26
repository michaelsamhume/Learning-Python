def check_password(test):
    #Is the password long enough? Does it have letters and numbers?
    if test == 'JohnCena1':
        print('Hello Michael')
        return True
    else:
        print('Incorrect password')
        return False




    def change_password(officialpassword):
        pwd = input('What is the current password?')
        if pwd == officialpassword:
            officialpassword = input('Pick your new password.')
        return officialpassword
    print('Bad password')
    return False

officialPassword = 'blahblah!'

pwd = input('Pick a password.\n')
if len(pwd)>8:
    good = check_password(pwd)
else:
    good = False
    print('Password too short.')
print('Password is good:' +str(good))