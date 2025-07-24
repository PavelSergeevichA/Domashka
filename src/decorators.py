from functools import wraps


def log(func):
    """Декоратор логирует работу функции и ее результат как в файл, так и в консоль"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        try:
            result = func(*args, **kwargs)
            print(f"{func_name} ok")
            return result
        except Exception as e:
            print(f"{func_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
            raise
    return wrapper
