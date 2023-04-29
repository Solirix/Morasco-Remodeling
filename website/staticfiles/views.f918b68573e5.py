from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Carousel
from .forms import ContactMe
from django.contrib import messages

# this will be the home page
def index(request):
    obj = Carousel.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'core/index.html', context)

# this will serve as the portfolios page
def portfolio(request):
    return render(request, 'core/portfolio.html')

# this will serve as the contact us page
def contact(request):
    if request.method == 'POST':
        form = ContactMe(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('index')
    else:
        form = ContactMe()

    return render(request, 'core/contact.html', {'form': form})


# this will serve as the about us page
def about(request):
    return render(request, 'core/about.html')

# this will serve the services page
def services(request):
    return render(request, 'core/services.html')
