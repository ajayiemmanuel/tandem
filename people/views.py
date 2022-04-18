from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *


@login_required (login_url = "login")
def index(request):
    context = {}
    return render (request, "people/index.html", context)


@login_required (login_url = "login")
def apply_loan(request):
    context = {}
    return render (request, "people/apply-loan.html", context)


@login_required (login_url = "login")
def animation(request):
    context = {}
    return render (request, "people/animation.html", context)


@login_required (login_url = "login")
def card(request):
    context = {}
    return render (request, "people/card.html", context)


@login_required (login_url = "login")
def charts(request):
    context = {}
    return render (request, "people/charts.html", context)


def forgot_password(request):
    context = {}
    return render (request, "people/forgot-password.html", context)


@login_required (login_url = "login")
def loan_status(request):
    context = {}
    return render (request, "people/loan-status.html", context)


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect ('index')
    else:
        if request.method == 'POST':
            username = request.POST.get ('username')
            password = request.POST.get ('password')

            user = authenticate (request, username = username, password = password)

            if user is not None:
                login (request, user)
                return redirect ('index')
            else:
                messages.info (request, 'Username OR password is incorrect')

        context = {}
    return render (request, "people/login.html", context)


def logoutUser(request):
    logout (request)
    return redirect ('login')


@login_required (login_url = "login")
def other(request):
    context = {}
    return render (request, "people/other.html", context)


def register(request):
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        form = CreateUserForm ()
        if request.method == 'POST':
            form = CreateUserForm (request.POST)
            if form.is_valid ():
                form.save ()
                user = form.cleaned_data.get ('username')
                messages.success (request, 'Account was created for ' + user)

                return redirect ('login')

        context = {'form': form}
    return render (request, "people/register.html", context)


@login_required (login_url = "login")
def transaction(request):
    context = {}
    return render (request, "people/transaction.html", context)


@login_required (login_url = "login")
def tranfer(request):
    context = {}
    return render (request, "people/tranfer.html", context)


@login_required (login_url = "login")
def blank(request):
    context = {}
    return render (request, "people/blank.html", context)
