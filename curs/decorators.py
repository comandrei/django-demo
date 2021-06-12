def view_counter(func):
    def wrapper(request):
        print("Decorator 2")
        request.session[request.path] = request.session.get(func.__name__, 0) + 1
        return func(request)
    return wrapper

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1")
        return func(*args, **kwargs)
    return wrapper
