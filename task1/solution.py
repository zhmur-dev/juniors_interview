def strict(func):
    def wrapper(*args, **kwargs):
        arg_names = tuple(func.__annotations__.keys())
        for arg in enumerate(args):
            arg_value = arg[1]
            annotation = func.__annotations__.get(arg_names[arg[0]])
            if not isinstance(arg_value, annotation):
                raise TypeError(
                    f'Argument value {arg_value} is not Type {annotation}'
                )
        result = func(*args, **kwargs)
        return result
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
