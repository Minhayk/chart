from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import ListView
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect,  get_object_or_404
from django.contrib import auth
from django.contrib.auth import models
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.core import serializers
from django.db import connection
# import sqlite3, random, os, json
from django.shortcuts import render
# from .forms import ClientForm
from .models import Genre, Movie
# from django.db.models import Avg, Max,F, FloatField, Sum,Count
import datetime
import calendar

# def home(request):
#     return render(request, 'templates/base.html',{})


def home(request):
    movie_animation=[]
    movie_action=[]
    movie_fantacy=[]
    movie_sci_fi=[]

    queryset = Movie.objects.all()
    movies_list=queryset.values_list('name', flat=True).distinct().order_by('-name')

    for i in range(len(movies_list)):
        genre_id = queryset.filter(name=movies_list[i]).values_list('genre_id')[0][0]
        genre_name = Genre.objects.filter(id=genre_id).values_list('name')[0][0]
        date = queryset.filter(name=movies_list[i]).values_list('date')[0][0]
        grossing = queryset.filter(name=movies_list[i]).values_list('grossing')[0][0]
        budget = queryset.filter(name=movies_list[i]).values_list('budget')[0][0]

        temp=dict()
        temp['name']=movies_list[i]
        temp['genre']=genre_name
        temp['year']=date
        temp['grossing']=grossing
        temp['budget']=budget
        if genre_id==1:
            movie_fantacy.append(temp)
        elif genre_id==2:
            movie_sci_fi.append(temp)
        elif genre_id==3:
            movie_action.append(temp)
        else:
            movie_animation.append(temp)


    return render(request, 'templates/base.html', {'movie_action': movie_action, 'movie_animation': movie_animation,
                                                   'movie_fantacy': movie_fantacy, 'movie_sci_fi': movie_sci_fi})

def annimation(request):
    movie_animation=[]
    movie_action=[]
    movie_fantacy=[]
    movie_sci_fi=[]

    queryset = Movie.objects.all()
    movies_list=queryset.values_list('name', flat=True).distinct().order_by('-name')

    for i in range(len(movies_list)):
        genre_id = queryset.filter(name=movies_list[i]).values_list('genre_id')[0][0]
        genre_name = Genre.objects.filter(id=genre_id).values_list('name')[0][0]
        date = queryset.filter(name=movies_list[i]).values_list('date')[0][0]
        grossing = queryset.filter(name=movies_list[i]).values_list('grossing')[0][0]
        budget = queryset.filter(name=movies_list[i]).values_list('budget')[0][0]

        temp=dict()
        temp['name']=movies_list[i]
        temp['genre']=genre_name
        temp['year']=date
        temp['grossing']=grossing
        temp['budget']=budget
        if genre_id==1:
            movie_fantacy.append(temp)
        elif genre_id==2:
            movie_sci_fi.append(temp)
        elif genre_id==3:
            movie_action.append(temp)
        else:
            movie_animation.append(temp)


    return render(request, 'templates/annimation.html', {'movie_action': movie_action, 'movie_animation': movie_animation,
                                                   'movie_fantacy': movie_fantacy, 'movie_sci_fi': movie_sci_fi})

def action(request):
    movie_animation=[]
    movie_action=[]
    movie_fantacy=[]
    movie_sci_fi=[]

    queryset = Movie.objects.all()
    movies_list=queryset.values_list('name', flat=True).distinct().order_by('-name')

    for i in range(len(movies_list)):
        genre_id = queryset.filter(name=movies_list[i]).values_list('genre_id')[0][0]
        genre_name = Genre.objects.filter(id=genre_id).values_list('name')[0][0]
        date = queryset.filter(name=movies_list[i]).values_list('date')[0][0]
        grossing = queryset.filter(name=movies_list[i]).values_list('grossing')[0][0]
        budget = queryset.filter(name=movies_list[i]).values_list('budget')[0][0]

        temp=dict()
        temp['name']=movies_list[i]
        temp['genre']=genre_name
        temp['year']=date
        temp['grossing']=grossing
        temp['budget']=budget
        if genre_id==1:
            movie_fantacy.append(temp)
        elif genre_id==2:
            movie_sci_fi.append(temp)
        elif genre_id==3:
            movie_action.append(temp)
        else:
            movie_animation.append(temp)


    return render(request, 'templates/action.html', {'movie_action': movie_action, 'movie_animation': movie_animation,
                                                   'movie_fantacy': movie_fantacy, 'movie_sci_fi': movie_sci_fi})

def sci_fi(request):
    movie_animation=[]
    movie_action=[]
    movie_fantacy=[]
    movie_sci_fi=[]

    queryset = Movie.objects.all()
    movies_list=queryset.values_list('name', flat=True).distinct().order_by('-name')

    for i in range(len(movies_list)):
        genre_id = queryset.filter(name=movies_list[i]).values_list('genre_id')[0][0]
        genre_name = Genre.objects.filter(id=genre_id).values_list('name')[0][0]
        date = queryset.filter(name=movies_list[i]).values_list('date')[0][0]
        grossing = queryset.filter(name=movies_list[i]).values_list('grossing')[0][0]
        budget = queryset.filter(name=movies_list[i]).values_list('budget')[0][0]

        temp=dict()
        temp['name']=movies_list[i]
        temp['genre']=genre_name
        temp['year']=date
        temp['grossing']=grossing
        temp['budget']=budget
        if genre_id==1:
            movie_fantacy.append(temp)
        elif genre_id==2:
            movie_sci_fi.append(temp)
        elif genre_id==3:
            movie_action.append(temp)
        else:
            movie_animation.append(temp)


    return render(request, 'templates/sci-fi.html', {'movie_action': movie_action, 'movie_animation': movie_animation,
                                                   'movie_fantacy': movie_fantacy, 'movie_sci_fi': movie_sci_fi})

def fantasy(request):
    movie_animation=[]
    movie_action=[]
    movie_fantacy=[]
    movie_sci_fi=[]

    queryset = Movie.objects.all()
    movies_list=queryset.values_list('name', flat=True).distinct().order_by('-name')

    for i in range(len(movies_list)):
        genre_id = queryset.filter(name=movies_list[i]).values_list('genre_id')[0][0]
        genre_name = Genre.objects.filter(id=genre_id).values_list('name')[0][0]
        date = queryset.filter(name=movies_list[i]).values_list('date')[0][0]
        grossing = queryset.filter(name=movies_list[i]).values_list('grossing')[0][0]
        budget = queryset.filter(name=movies_list[i]).values_list('budget')[0][0]

        temp=dict()
        temp['name']=movies_list[i]
        temp['genre']=genre_name
        temp['year']=date
        temp['grossing']=grossing
        temp['budget']=budget
        if genre_id==1:
            movie_fantacy.append(temp)
        elif genre_id==2:
            movie_sci_fi.append(temp)
        elif genre_id==3:
            movie_action.append(temp)
        else:
            movie_animation.append(temp)


    return render(request, 'templates/fantacy.html', {'movie_action': movie_action, 'movie_animation': movie_animation,
                                                   'movie_fantacy': movie_fantacy, 'movie_sci_fi': movie_sci_fi})
