from django.shortcuts import render

def index(request):
    context = {
        'name': 'Артём' 
    }

    return render(request, 'expenses/index.html', context)