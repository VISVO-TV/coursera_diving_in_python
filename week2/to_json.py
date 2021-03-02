"""Задание по программированию: Декоратор to_json"""

def to_json(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return { func.__name__: result }
    return wrapped


@to_json
def any_func(a, b):
    return a, b


# Тест декоратора функции
print(any_func(10, 12))
