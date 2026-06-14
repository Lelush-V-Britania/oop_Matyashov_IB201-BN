def check_password(expected_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            password = input("Введите пароль: ")
            if password == expected_password:
                return func(*args, **kwargs)
            else:
                print("В доступе отказано")
                return None
        return wrapper
    return decorator

@check_password("password")
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    print(f"Готовим бургер с мясом: {typeOfMeat}")
    print(f"Лук: {'да' if withOnion else 'нет'}")
    print(f"Помидоры: {'да' if withTomato else 'нет'}")
    return "Бургер готов!"