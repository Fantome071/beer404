from django.shortcuts import render


from datetime import datetime
from pprint import pprint


def index(request):
  return render(request, 'event/index.html')
