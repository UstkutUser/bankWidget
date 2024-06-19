def log(filename=""):
    def wrapper(function):
        def inner(*args, **kwargs):
            try:
                message_ok = f"{function.__name__} ok"
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{message_ok}\n")
                else:
                    print(f"{message_ok}")
                return result
            except Exception as e:
                message_err = f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{message_err}\n")
                else:
                    print(f"{message_err}")
        return inner
    return wrapper


@log(filename="log.txt")
def func(a, b):
    return a / b

func(2,0)