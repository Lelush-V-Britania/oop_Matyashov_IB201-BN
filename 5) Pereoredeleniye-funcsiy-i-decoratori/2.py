def check_password(func):
    def wrapper(n):
        password = input("Введите пароль: ")
        if password == "8902":
            return func(n)
        else:
            print("В доступе отказано")
            return None
    return wrapper

@check_password
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)