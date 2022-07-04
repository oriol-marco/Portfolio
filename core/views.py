
from django.shortcuts import render

from django.conf import settings
from .models import Home, About, Profile, Category, Portfolio, Contact


from django.http import HttpResponse


# Create your views here.

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    # Contact
    contact = Contact.objects.all()

    
    context = {
        'home' : home,
        'about' : about,
        'profiles' : profiles,
        'categories' : categories,
        'portfolios' : portfolios,
    }

        
    if request.method == 'POST':
            contact = Contact()
            name = request.POST.get('name')
            email = request.POST.get('email')
            text = request.POST.get('text')
            contact.name = name
            contact.email = email
            contact.text = text
            contact.save()
            return HttpResponse("<h1>Thanks for contact</h1>")


    return render(request, 'index.html', context)
