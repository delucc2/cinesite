from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def policies(request):
    return render(request, 'home/policies.html')


def requests(request):
    return render(request, 'home/requests.html')


def feedback(request):
    return render(request, 'home/feedback.html')


def login(request):
    return render(request, 'home/login.html')