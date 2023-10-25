from django.shortcuts import render


def hello(request):
    context = {
        'name': 'John',
        'last_name': 'Doe',
    }
    return render(request, 'hello.html', context)


def goodbye(request):
    return render(request, 'goodbye.html')