from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache


def sign_in_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,'Invalid Session')
            return redirect('signin')
        
        else:
            return fn(request,*args,**kwargs)
        
    return wrapper


rule=[sign_in_required,never_cache]