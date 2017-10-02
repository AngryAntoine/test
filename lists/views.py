from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from .models import Item


def home_page(request):
    items = Item.objects.all()
    if request.method == 'POST':
        Item.objects.create(text=request.POST.get('item_text'))
        return redirect('lists:home_page')
    return render(request, 'lists/home.html', locals())


