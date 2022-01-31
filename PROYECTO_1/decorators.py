from unittest import result


PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password = input('Cual es tuy contrasena? ')

        if password == PASSWORD:
            return func()
        else:
            print('La contrasena no es correcta.')
    
    return wrapper

@password_required
def needs_password():
    print('La contrasena es correcta')


def upper(func):
    def wrapper(*args, **kwars):
        result = func(*args, **kwars)

        return result.upper()

    return wrapper

@upper
def say_my_name(name):
    return('Hola, {}'.format(name))


if __name__ == '__main__':
    print(say_my_name('Anderson'))