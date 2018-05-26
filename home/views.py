from django.shortcuts import render
from info.models import Movie


# View for homepage (Schedule tab)
def index(request):
    upcoming_showings = Movie.upcoming_movies
    context = {'showings': upcoming_showings}
    return render(request, 'home/index.html', context)


# View for Policies and Bylaws tab
def policies(request):
    return render(request, 'home/policies.html')


# View for Requests tab
def requests(request):
    return render(request, 'home/requests.html')


# View for Feedback/FAQ tab
def feedback(request):
    return render(request, 'home/feedback.html')


# View for login page
def login(request):
    return render(request, 'home/login.html')