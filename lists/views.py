from django.shortcuts import render

# Create your views here.


def home(request):
    title = 'Obey the Testing Goat!'
    return render(request, 'lists/home.html', locals())
