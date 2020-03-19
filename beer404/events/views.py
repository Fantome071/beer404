from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.db.models import Avg
from django.db.models import Count
from django.contrib.auth import get_user_model

from datetime import datetime
from pprint import pprint

from .models import User
from .models import Event


def index(request):
  return render(request, 'event/index.html')

@login_required
def logout_view(request):
  logout(request)
  return redirect('index')

def register_view(request):
  return render(request, 'event/register.html')

def login_view(request):
  return render(request, 'event/login.html')
