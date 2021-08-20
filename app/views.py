from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'saiee','age':22}
    return render(request, 'loop.html',d)