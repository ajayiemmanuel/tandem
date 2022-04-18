from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path ('', views.index, name = "index"),
    path ('apply_loan/', views.apply_loan, name = "apply-loan"),
    path ('card/', views.card, name = "card"),
    path ('charts/', views.charts, name = "charts"),
    path ('forgot_password/', views.forgot_password, name = "forgot-password"),
    path ('loan_status/', views.loan_status, name = "loan-status"),
    path ('login/', views.LoginPage, name = "login"),
    path ('logout/', views.logoutUser, name = "logout"),
    path ('register/', views.register, name = "register"),
    path ('transaction/', views.transaction, name = "transaction"),
    path ('tranfer/', views.tranfer, name = "tranfer"),
    path ('animation/', views.animation, name = "animation"),
    path ('blank/', views.blank, name = "blank"),

    ]