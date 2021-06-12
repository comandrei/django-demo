def simple_middleware(get_response):
    print("middleware setup")
    def middleware(request):
        print("Request")
        request.custom = 10
        response = get_response(request)
        print("Response")
        return response
    return middleware
