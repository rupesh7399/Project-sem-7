from django.contrib import admin
from django.urls import path , include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="home"),
    path('profile',views.profile,name ='profile'),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
    path('home',views.home,name="home"),
    path('logout',views.logout,name="logout"),
    path('about',views.about,name="about"),
    path('check_login', views.check_login, name="check_login"),
    path('check_email', views.check_email, name="check_email"),
    path('data',views.data,name="data"),
    path('data.html',views.data,name="data"),
    path('gh',views.data,name="data"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('reports',views.reports,name="reports"),
    path('W_delete<int:id>',views.W_delete,name="W_delete"),
    path('filter',views.filter,name="filter"),
    path('markov',views.markov,name="markov"),
    path('descriptive',views.descriptive,name="descriptive"),
    path('desAnalysis',views.desAnalysis,name="desAnalysis"),
    path('changepass',views.changepass,name="changepass"),
    path('chake',views.chake,name="chake"),
    path('MarkovProcess',views.MarkovProcess,name="MarkovProcess"),
    path('data_table',views.data_table,name="data_table"),
    path('For_Pass',views.For_Pass,name="For_Pass"),
    path('send',views.send,name="send"),
    
        
    
    
    
    
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_URL)
# https://ruddra.com/posts/deploy-django-to-openshift-3/