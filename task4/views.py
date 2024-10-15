from django.shortcuts import render

# Create your views here.
# python manage.py runserver

def films(request):
    return render(request, 'main.html')

def cinemas(request):
    context ={
        'my_films': ['Американский пирог', 'Американский пирог 2', 'Американский пирог 3']
    }
    return render(request, 'cinema.html', context)

def tickets(request):
    return render(request, 'ticket.html')