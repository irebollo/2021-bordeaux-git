def get_credentials():
    username = input('Type the username: ')
    password = input('Type the password: ')
    return username, password

def authenticate(user, password, pwdb):
    if user in pwdb:
        if password == pwdb[user]:
            print('Successfully authenticated!')
        else:
            print('Wrong password!!')
    else:
        add = input('Add user to the db? ')
        if add == 'y':
            pwdb[user] = password
        else:
            pass
    return

print(get_credentials())

