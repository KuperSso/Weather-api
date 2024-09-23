import requests
from django.shortcuts import render
from .forms import CityForm

def index(request):
    app_id = 'bc99468d969c8385852eb72fd14f4732'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=' + app_id

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

        form = CityForm
    
    city = 'Krasnodar'
    res = requests.get(url.format(city)).json()

    city_info = {
        'city': city,
        'temp': res['main']['temp'],
        'icon': res['weather'][0]['icon'],
        'wind': res['wind']['speed']
    }

    context = {'info': city_info, 'form':form}

    return render(request, 'weather_welcome.html', context)
