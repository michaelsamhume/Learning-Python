def set_password(journal):
    if len(journal[0]) > 0:
        print('This journal already has a password.')
        menu(journal)
    else:
        journal[0] = input('Set a password for your journal.')
        menu(journal)


def change_password(journal):
    pwd = input('Please enter current password.')
    if pwd == journal[0]:
        journal[0] = input('Please enter a new password.')
        menu(journal)
    else:
        print('Password incorrect.')
        menu(journal)


def set_message(journal):
    pwd = input('Please enter current password.')
    if pwd == journal[0]:
        journal[1] = input('Please enter desired message.')
    if len(journal[1]) > 0:
        print('message successful')
    menu(journal)


def read_message(journal):
    pwd = input('Please enter current password.')
    if pwd == journal[0]:
        if len(journal[1]) > 0:
            print(journal[1])
        menu(journal)
    else:
        print('No available Entry')
        menu(journal)


def menu(journal):
    option = int(input('1) Set password.\n'
                       '2) Change password\n'
                       '3) Set message \n'
                       '4) Read message \n'
                       '5) Exit \n'
                       ))
    if option == 1:
        set_password(journal)
    elif option == 2:
        change_password(journal)
    elif option == 3:
        set_message(journal)
    elif option == 4:
        read_message(journal)
    elif option == 5:
        return


if __name__ == '__main__':
    password = ''
    message = ''
    journal = [password, message]
    menu(journal)
