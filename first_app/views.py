from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me': "this allows me to put stuff into the html through python that's kinda cool"}
    return render(request, 'first_app/index.html', context=my_dict)

# Create your views here.
