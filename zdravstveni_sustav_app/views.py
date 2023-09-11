from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate, login
from users.forms import LoginForm

# Create your views here.
def pocetna(request):
    return render(request, 'zdravstveni_sustav_app/pocetna.html')

def about(request):
    doktori = Doktor.objects.all()
    return render(request, 'zdravstveni_sustav_app/about.html', {'doktori':doktori})

def lokacije(request):
    lokacije = DomZdravlja.objects.all()
    return render(request, 'zdravstveni_sustav_app/lokacije.html', {'lokacije':lokacije})

def not_found(request):
    return HttpResponseNotFound('<h1>Stranica nije pronađena</h1>')

def doktori(request):
    doktori = Doktor.objects.all()
    return render(request, 'zdravstveni_sustav_app/doktori.html', {'doktori':doktori})

"""
First make sure you have SessionMiddleware and AuthenticationMiddleware middlewares added to your MIDDLEWARE_CLASSES setting.
The current user is in request object, you can get it by:
request.user will give you a User object representing the currently logged-in user. 
If a user isn't currently logged in, request.user will be set to an instance of AnonymousUser. 
You can tell them apart with the field is_authenticated, like so:

if request.user.is_authenticated:
    # Do something for authenticated users.
else:
    # Do something for anonymous users.
"""
def termini(request):
    trenutni_korisnik = request.user
    trenutni_korisnik_id = trenutni_korisnik.id
    doktor = Doktor.objects.get(id=trenutni_korisnik_id)
    narudzba_set = doktor.narudzba_set.all()
    #narudzbe = Narudzba.objects.all()
    context = {
        'doktor':doktor,
        'narudzba_set':narudzba_set,
    }
    return render(request, 'zdravstveni_sustav_app/termini.html', context)

"""
def my_view(request):
    if request.method == 'POST':
        # username = request.POST["username"]
        # password = request.POST["password"]
        form = LoginForm(request.POST)
        user = authenticate(request, username=form.username, password=form.password)
        if user is not None:
            login(request, user)
            #messages.success(request, "Uspjesna prijava!")  # Success message
            return redirect('/')  # Redirect to the home page or any other desired URL name
        else:
            messages.error(request, "Neispravan unos, pokušajte ponovno.")  # Error message
    return render(request, 'users/login.html', {'form':form})  # Render the login form template
"""

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Bind the form with POST data

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page or perform other actions
                return redirect('/')
            else:
                messages.error(request, 'Pogrešno korisničko ime ili lozinka. Pokušajte ponovno.')
        else:
            messages.error(request, 'Form validation failed. Please check your inputs.')
    else:
        form = LoginForm()  # Create an instance of the login form

    return render(request, 'users/login.html', {'form': form})


# def narudzba(request):
#     return render(request, 'zdravstveni_sustav_app/narudzba.html')

class NarudzbaView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'doktori': Doktor.objects.all()
        }
        return render(request, "zdravstveni_sustav_app/narudzba.html", context)

    def post(self, request, *args, **kwargs):
        ime_pacijenta = request.POST.get('ime_pacijenta')
        prezime_pacijenta = request.POST.get('prezime_pacijenta')
        telefon_pacijenta = request.POST.get('telefon_pacijenta')
        email_pacijenta = request.POST.get('email_pacijenta')
        doktor_id = request.POST.get('doktor')
        datum_pregleda = request.POST.get('datum_pregleda')
        vrijeme_pregleda = request.POST.get('vrijeme_pregleda')
        simptomi = request.POST.get('simptomi')
        if doktor_id:
            doktor = get_object_or_404(Doktor, id=doktor_id)

        if(ime_pacijenta and prezime_pacijenta and email_pacijenta and doktor and datum_pregleda and vrijeme_pregleda):
            Narudzba.objects.create(
                ime_pacijenta=ime_pacijenta, 
                prezime_pacijenta=prezime_pacijenta, 
                telefon_pacijenta=telefon_pacijenta,
                email_pacijenta=email_pacijenta, 
                doktor=doktor, 
                datum_pregleda=datum_pregleda, 
                vrijeme_pregleda=vrijeme_pregleda,
                simptomi=simptomi
                )
            
            messages.success(request,'Uspješna prijava narudžbe!')
        return redirect('narudzba')