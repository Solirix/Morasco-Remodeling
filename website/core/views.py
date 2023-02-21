from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> respinse
# request handler

# this will be the home page
def index(request):
    return render(request, 'core/index.html')

# this will serve as the portfolios page
def portfolio(request):
    return render(request, 'core/portfolio.html')