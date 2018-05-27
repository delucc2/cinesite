from django.shortcuts import render
from info.models import Movie, Officers
from datetime import date


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
    officers = Officers.objects.get(year=date.today().year)
    chair = officers.chair
    fnc = officers.fnc
    snc = officers.snc
    mw = officers.mw
    rep = officers.rep
    pub = officers.pub
    web = officers.web
    proj = officers.projectionists.all()

    context = {'chair': chair,
               'friday': fnc,
               'saturday': snc,
               'midweek': mw,
               'rep': rep,
               'publicity': pub,
               'webmaster': web,
               'projectionists': proj}

    return render(request, 'home/feedback.html', context)


# View for login page
def login(request):
    return render(request, 'home/login.html')