from django.contrib import admin
from django.urls import path
from . import views
  
urlpatterns = [
    path("", views.index,name='index'),
    path("login2/", views.login2,name='login2'),
    path("login2/signin/", views.signin,name='signin'),
    # path("index/login2/signin/incorrect", views.incorrect,name='login2'),
    path("login2/signup/", views.sign,name='sign'),
    path("login2/signup/back/",views.back,name='back'),
    path('login2/signup/createuser/',views.createuser,name="createuser"),
    path("login2/signin/predict/", views.predict,name='predict'),
    path("login2/signin/predict/result", views.result),
    path("login2/signin/predict/result/output/", views.output),
    path("login2/signin/predict/home/", views.home),
    path("login2/signin/predict/home/back2/", views.back2),
    # path("index/login2/predict/data/",views.data,name ="data"),
]
