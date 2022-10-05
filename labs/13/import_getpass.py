import getpass
user = getpass.getuser()
password = getpass.getpass()
def svc_login(user, password):
    print(f'Logging in as {user}')
    # TODO: check if user/password is valid
    return True

if svc_login(user, password) == True:
    print(f'Successfully logged in as {user}')
else:
    print(f'Failed to log in')