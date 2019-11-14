"""Feedback_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Feedback_home import views

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('',views.showIndex,name="main"),
    path('login/',views.login,name="login"),
    path('registration/',views.register,name="register"),
    path('home/',views.home,name="home"),
    path('aboutUs/',views.aboutUs,name="aboutUs"),
    path('contact_us/',views.contactUs,name='contact_us'),
    path('getRegister/',views.getRegister,name='getRegister'),
    path('saveFaculty/',views.saveFaculty,name='saveFaculty'),
    path('saveStudent/',views.saveStudent,name='saveStudent'),
    path('loginFS/',views.loginFacultyStudent,name='loginFS'),
    path('logout/',views.logout,name='logout'),
    path('saveFeedback/',views.saveFeedback,name='saveFeedback'),
    path('logoutf/',views.logoutf,name='logoutf'),
    path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
    path('downloadfeedback/',views.downloadfeedback,name='downloadfeedback'),
    path('dc/',views.dc,name="dc"),
    path('AddFaculty/',views.addFaculty,name='addf'),
    path('AddFaculty1/', views.addFaculty1, name='Addf1')
]
