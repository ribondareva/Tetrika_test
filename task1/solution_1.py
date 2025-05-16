def strict(func):
    ann = func.__annotations__
    pos_names = func.__code__.co_varnames[:func.__code__.co_argcount]

    def wrapper(*args, **kwargs):
        for name, value in zip(pos_names, args):
            expected = ann.get(name)
            if expected and type(value) is not expected:
                raise TypeError(
                    f'Аргумент {name} ожидает {expected.__name__}, '
                    f'получено {type(value).__name__}'
                )
        for name, value in kwargs.items():
            expected = ann.get(name)
            if expected and type(value) is not expected:
                raise TypeError(
                    f'Аргумент {name} ожидает {expected.__name__}, '
                    f'получено {type(value).__name__}'
                )
        return func(*args, **kwargs)

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError
