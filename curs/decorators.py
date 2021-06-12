def view_counter(func):
    def wrapper(request):
        request.session[request.path] = request.session.get(func.__name__, 0) + 1
        return func(request)
    return wrapper