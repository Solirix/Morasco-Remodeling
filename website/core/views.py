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

# this will serve as the contact us page
def contact(request):
    return render(request, 'core/contact.html')

# this will serve as the about us page
def about(request):
    return render(request, 'core/about.html')

# this will serve the services page
def services(request):
    return render(request, 'core/services.html')
