original_print = print

def print(*args, **kwargs):
    upper_args = [str(arg).upper() for arg in args]
    original_print(*upper_args, **kwargs)