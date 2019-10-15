import xlrd

from django.db import models
import csv , io
from django.shortcuts import render
from django.http import HttpResponse
from test1.models import weather_data
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

# Create your views here.
def upload(request):
    if request.method == 'POST':
        Name = request.POST['file1']
        return Name

    else:
        return render(request,'upload.html')


