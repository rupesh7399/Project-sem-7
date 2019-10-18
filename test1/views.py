from django.contrib.auth.decorators import login_required, permission_required
from django.db.models.query import EmptyQuerySet
import numpy as np
import pandas_datareader as pr
import pandas as pd
import datetime
import xlrd
import sqlite3
from django.shortcuts import render,redirect
from django.http import HttpResponse , JsonResponse
from django.contrib.auth.models import User, auth 
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
# from django.core.exceptions import ObjectDoesNotExit
from django.http import Http404 
from .models import *
from django_pandas.io import read_frame
import csv,io
import reportlab
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from scipy import stats
import scipy
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
import matplotlib.pyplot as plt
from pylab import *
from chartit import DataPool, Chart
import json
#import win32api
from jinja2 import Environment, FileSystemLoader
#from weasyprint import HTML

#############################################
#----------ABOUT----------------------------#
#############################################

def about(request):
    return render(request,'aboutus.html')
# Create your views here.
def home(request):
    
    return render(request,'home.html')

####################################################
# ----------------Loging---------------------------#
####################################################

def login(request):
   if request.method == 'POST':
       username = request.POST['email']
       password = request.POST['password']
       user = auth.authenticate(username=username,password=password)
       
       if user is not None:
           auth.login(request,user)
           
           return redirect("/")
       else:
           messages.info(request,'invelid credentials!!')
           return render(request,'login.html')

   else:
     return render(request,'login.html')

#########################################
#-----------register--------------------#
#########################################
    
def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        user.save()
        messages.info(request,'Successful Registation!!')
        return redirect('register')
    else:
        return render(request,'register.html')

###########################################
# ------------- Profile-------------------#
###########################################

def profile(request):
    if request.user.is_superuser :
        redirect('admin')
    else:
        return render(request,'profile.html')

############################
# -----------logout------- #
############################
def logout(request):
    auth.logout(request)
    return redirect('/')

######################################
#------- Chake Login                 #
######################################
def check_login(request):
    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:   
        response_data = {}
        login = request.POST["uname"]
        user = None
        try:
            try:
                # we are matching the input again hardcoded value to avoid use of DB.
                # You can use DB and fetch value from table and proceed accordingly.
                if User.objects.filter(username=login).exists():
                    user = True
            except ObjectDoesNotExist as e:
                pass
            except Exception as e:
                raise e
            if not user:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        except Exception as e:
            response_data["is_success"] = False
            response_data["msg"] = "Some error occurred. Please let Admin know."

        return JsonResponse(response_data)

####################################
# --------check_email--------------#
####################################

def check_email(request):
    if request.method == "GET":
        raise Http404("URL doesn't exists")
    else:   
        response_data = {}
        login = request.POST["email"]
        user = None
        try:
            try:
                # we are matching the input again hardcoded value to avoid use of DB.
                # You can use DB and fetch value from table and proceed accordingly.
                if User.objects.filter(email=login).exists():
                    user = True
            except ObjectDoesNotExist as e:
                pass
            except Exception as e:
                raise e
            if not user:
                response_data["is_success"] = True
            else:
                response_data["is_success"] = False
        except Exception as e:
            response_data["is_success"] = False
            response_data["msg"] = "Some error occurred. Please let Admin know."

        return JsonResponse(response_data)

###################################
#-------------DATA---------------#
###################################

def data(request):
    data = weather_data.objects.all()
    
    return render(request,"data.html",locals())



###################################
# ----- Reports ------------------#
###################################

def reports(request):
    return render(request,"reports.html")

##################################
#-----Weather Data Delete--------#
##################################
def W_delete(request,id):
    weather_data.objects.get(id=id).delete()
    return redirect("data.html")

##################################
#----------report search---------#
##################################
import pdfkit

def filter(request):
    date_min = request.POST.get('date_min')
    date_max = request.POST.get('date_max')
    filter_type = request.POST.get('data')


    qs = weather_data.pdobjects.filter(DATE__range=(date_min,date_max))

    if filter_type == "Month":
        df = read_frame(qs)
        df['Date'] = pd.to_datetime(df['DATE'], errors='coerce')
        df['Month_Number'] = df['Date'].dt.month
        df['Year'] = df['Date'].dt.year
        df = df.groupby(['Year','Month_Number']).agg({'ET':'max','EP':'max','BSS':'max','RF':'max','WS':'max','DT1':'max','WT1':'max','DT2':'max','WT2':'max','MAXT':'max','MINT':'max','RH11':'max','RH22':'max','VP11':'max','VP11':'max','CLOUDM':'max','CLOUDE':'max','SOIL1':'max','SOIL2':'max','SOIL3':'max','SOIL4':'max','SOIL5':'max','SOIL6':'max','MinTtest':'max','MaxTtest1':'max','MaxTtest2':'max'})
        return HttpResponse(df.to_html())
    elif filter_type == "weekly":
        df = read_frame(qs)
        df['Date'] = pd.to_datetime(df['DATE'], errors='coerce')
        df['Week_Number'] = df['Date'].dt.week
        df['Year'] = df['Date'].dt.year
        df = df.groupby(['Year','Week_Number']).agg({'ET':'sum','EP':'sum','BSS':'sum','RF':'sum','WS':'sum','DT1':'sum','WT1':'sum','DT2':'sum','WT2':'sum','MAXT':'sum','MINT':'sum','RH11':'sum','RH22':'sum','VP11':'sum','VP11':'sum','CLOUDM':'sum','CLOUDE':'sum','SOIL1':'sum','SOIL2':'sum','SOIL3':'sum','SOIL4':'sum','SOIL5':'sum','SOIL6':'sum','MinTtest':'sum','MaxTtest1':'sum','MaxTtest2':'sum'})
        return HttpResponse(df.to_html())
    else:
        return render(request,"reports.html",locals())
    

# hint: https://stackoverflow.com/questions/4668619/how-do-i-filter-query-objects-by-date-range-in-django  

# range =pd.date_range(start=date_min, end=date_max, periods=None, freq='D')
    # # range = pd.date_range(date_min, date_max,dtype='datetime64[ns]',freq='D')
    # df = qs.DataFrame(index = range)
    # df = qs.DataFrame(fieldnames=['id','ET','EP','BSS','RF','WD','WD1','WS','DT1','WT1','DT2','WT2','MAXT','MINT','RH11','RH22','VP11','VP11','CLOUDM','CLOUDE','SOIL1','SOIL2','SOIL3','SOIL4','SOIL5','SOIL6','MinTtest','MaxTtest1','MaxTtest2'],index = 'DATE')
    
    # weekly_summary['ET'] = df.ET.resample('W').mean()
    # weekly_summary = weekly_summary.truncate(before=date_min, after=date_max)
    # qs = weekly_summary.head()

    # date = df[1];et = df[2];EP = df[3];BSS = df[4]; RF = df[5];WD = df[6];WD1=df[7];WS=df[8];DT1=df[9];WT1=df[10];DT2=df[11];WT2=df[12];MAXT=df[13];MINT=df[14];RH11=df[15];RH22=df[16];VP11=df[17];VP11=df[18];CLOUDM=df[19];CLOUDE=df[20];SOIL1=df[21];SOIL2=df[22];SOIL3=df[23];SOIL4=df[24];SOIL5=df[25];SOIL6=df[26];MinTtest=df[27];MaxTtest1=df[28];MaxTtest2=df[29]
################################
# ------- Page of markov chain-#
################################

def markov(request):
    return render(request,"markov.html")

###############################################
###-----change Password---------------------###
###############################################
@login_required
def changepass(request):
    return render(request,"changepass.html")
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
def chake(request):
    old = request.POST['email']
    new = request.POST['password']
    username = request.user.username
    user = authenticate(username=username, password=old)
    if user is not None:
        u = User.objects.get(username=username)
        u.set_password(new)
        u.save()
        messages.info(request,'Password is successfully change!!')
    else:
        messages.info(request,'Old password is Wrond !!')        

    return render(request,"changepass.html",)
##----------------End -----------------------------------------------------#


######################################
#---Discriptive Analysis--############
######################################

def descriptive(request):
    return render(request,"descriptive.html")

########################################
#-----Dscriptive Analysis Process code-#
########################################

def desAnalysis(request):
    date_min = request.POST.get('date_min')
    date_max = request.POST.get('date_max')
    
    qs = weather_data.pdobjects.filter(DATE__range=(date_min,date_max))
    df = read_frame(qs)
    df = df.copy()
    df = df.loc[:,['RF']]
    m = np.mean(df)
    mi = df.median()
    mo = stats.mode(df)
    min = df.min()
    max = df.max()
    var = np.var(df)
    std = np.std(df)
    skew = scipy.stats.skew(df)
    ku = scipy.stats.kurtosis(df)
    a=np.percentile(df,100,axis=0, interpolation='lower')
    from scipy.stats import iqr
    b=iqr(df, axis=0 , rng=(25, 75), interpolation='lower')

    
    return render(request,"descriptiveanswer.html",locals())


############################################################
###########--Start Markov Chain process--###################
############################################################
from django.template.loader import render_to_string
def MarkovProcess(request):
    date_min = request.POST.get('date_min')
    date_max = request.POST.get('date_max')
    
    qs = weather_data.pdobjects.filter(DATE__range=(date_min,date_max))
    df = read_frame(qs)
    df = df.copy()
    df = df.loc[:,['DATE','RF']]
    df['Date'] = pd.to_datetime(df['DATE'], errors='coerce')
    df.index = pd.to_datetime(df.index,unit='D')
    df = df.asfreq('W').ffill()
    df['P'] = df['RF'].apply(lambda x: 1 if x >= 1 else 0)
    df = df.loc[:,['Date','P']]
    df = df.asfreq('W').ffill()
    df.reset_index(drop=True, inplace=True)
    df = df.sort_values('Date')
    df.reset_index(drop=True, inplace=True)
    l = ['year','weekofyear']
    df = df.join(pd.concat((getattr(df['Date'].dt, i).rename(i) for i in l), axis=1))
    df = df.loc[:,['weekofyear','P']]
    df['sec'] = df.P.shift(1)
    def analysis(df):
        if (df['P'] == 0 and df['sec']==0):
            return 'DD'
        elif (df['P'] == 0 and df['sec']==1):
            return 'DW'
        elif (df['P'] == 1 and df['sec']==0):
            return 'WD'
        elif (df['P'] == 1 and df['sec']==1):
            return 'WW'
    df['N'] = df.apply(analysis,axis = 1)
    #df = pd.get_dummies(df.set_index('NO')['P']).max(level=0).reset_index()
    df = df.groupby('weekofyear').N.value_counts().unstack().fillna(0)
    df['N0'] = df['DD'] + df['WD']
    df['N1'] = df['DW'] + df['WW']
    df['PDD'] = df['DD'] / df['N0']
    df['PDW'] = df['WD'] / df['N0']
    df['PWD'] = df['DW'] / df['N1']
    df['PWW'] = df['WW'] / df['N1']
    df['PD'] = df['DD'] + df['WD'] / df['N0'] + df['N1']
    df['PW'] = df['DW'] + df['WW'] / df['N0'] + df['N1']
    #df = df.loc[:,['P(W)','P(W/W)','W/D']]
    df = df.fillna(0)
    df = df.round(2)
    N0 = df.loc[:,['N0']].values.tolist()
    N1 = df.loc[:,['N1']].values.tolist()
    DD = df.loc[:,['PDD']].values.tolist()
    DW = df.loc[:,['PDW']].values.tolist()
    W = df.loc[:,['PW']].values.tolist()
    WW = df.loc[:,['PWW']].values.tolist()
    WD = df.loc[:,['WD']].values.tolist()
    PD = df.loc[:,['PD']].values.tolist()
    
    week = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52']
    week = pd.DataFrame(week).values.tolist()
    
    
   
    return render(request,"markovreport.html",{
        'PW' : json.dumps(W),
        'week': json.dumps(week),
        'PWW': json.dumps(WW),
        'PWD': json.dumps(WD),
        'N0' : json.dumps(N0),
        'N1' : json.dumps(N1),
        'DD' : json.dumps(DD),
        'DW' : json.dumps(DW),
        
        
    })
###########################################################
#-----------dataTable-------------------------------------#
###########################################################