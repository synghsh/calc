from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def history(request):
    return render(request, "history.html")

def aboutUs(request):
    return render(request, "aboutUs.html")

def calc(request):
    result = 0
    try:
        n1 = int(request.GET.get('num1')) 
        n2 = int(request.GET.get('num2'))
        if 'add' in request.GET:
            result = n1+n2 
        elif 'sub' in request.GET:
            result = n1-n2
        
        elif 'mul' in request.GET:
            result = n1*n2
        elif 'div' in request.GET:
            result = n1/n2
        else :
            print('error')
    except:
        pass
    return render(request, "calc.html", {'output':result})
    