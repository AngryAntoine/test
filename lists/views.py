from django.shortcuts import render

# Create your views here.


def home_page(request):
    title = 'Obey the Testing Goat!'
    context = {'title': title,
               'new_item_text': request.POST.get('item_text', '')
               }
    return render(request, 'lists/home.html', context)

