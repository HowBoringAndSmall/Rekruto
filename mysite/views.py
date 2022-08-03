from django.shortcuts import render


def home(request):
    name = 'Rekruto'
    message = 'Давай дружить!'
    return render(request, 'home.html', {'name': name, 'message': message})


def hello(request):
    msg = request.GET['message']
    return render(request, 'anotherpage.html', {'message': msg})