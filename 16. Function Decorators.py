def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper


@log_function_call
def say_hello():
    print("Hello there!")
    pass


# Using @log_function_call is the same as writing:
# say_hello = log_function_call(say_hello)

say_hello()