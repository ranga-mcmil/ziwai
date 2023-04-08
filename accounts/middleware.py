from django.shortcuts import render, get_object_or_404, redirect, reverse


def last_login_middleware(get_response):

    def middleware(request):
        response = get_response(request)

        print('/////////')
        if request.user.is_authenticated:
            if request.user.last_login == None and request.path != reverse('accounts:reset_password'):
                return redirect('accounts:reset_password')
        
        return response 
        
    return middleware