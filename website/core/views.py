from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> respinse
# request handler

def index(request):
    return render(request, 'core/index.html')

def portfolio(request):
    return render(request, 'core/portfolio.html')