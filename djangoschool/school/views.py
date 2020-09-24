from django.shortcuts import render
from django.http import HttpResponse

def HomePage(request):
    # return HttpResponse("<h1>inter</h1>")
    return render(request, 'school/home.html')