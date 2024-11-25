from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from django.contrib.auth.models import User

# Create your views here.

def index(request):
    num_visits = request.session.get('num_visits', 0)
    num_visits = num_visits + 1
    request.session['num_visits'] = num_visits
    template = loader.get_template('accounts/login.html')

    context = {
        'num_visits': num_visits,
    }
    #return HttpResponse(template.render())
    return render(request, 'accounts/login.html', context)

def create_user(request):
    user = User.objects.create_user("test01", "test01@greenextra.online", "123456")
    