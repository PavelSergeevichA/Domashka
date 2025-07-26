def log(filename=None):
    """Декоратор логирует работу функции и ее результат как в файл, так и в консоль"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            func_name = func.__name__
            if filename:  # Если задано имя файла для записи логов, записываем логи в файл
                try:
                    result = func(*args, **kwargs)
                    with open(filename, 'a') as f:
                        f.write(f"{func_name} ok\n")
                    return result
                except Exception as e:
                    with open(filename, 'a') as f:
                        f.write(f"{func_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n")
                    raise
            else:
                try:
                    result = func(*args, **kwargs)
                    print(f"{func_name} ok")
                    return result
                except Exception as e:
                    print(f"{func_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                    raise

        return wrapper  # Возвращаем обертку
    return decorator  # Возвращаем декоратор
