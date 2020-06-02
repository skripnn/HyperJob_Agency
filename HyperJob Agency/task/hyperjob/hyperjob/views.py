from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView



class Menu(View):
    menu_links = {
        'Login': '/login',
        'Sign up': '/signup',
        'Vacancies': '/vacancies',
        'Resumes': '/resumes',
        'Personal profile': '/home'
    }

    def get(self, request):
        return render(request, 'hyperjob/menu.html', context={'menu_links': self.menu_links})


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'hyperjob/signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'hyperjob/login.html'


class Home(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/')

        if request.user.is_staff:
            text = 'vacancy'
        else:
            text = 'resume'

        return render(request, 'hyperjob/home.html', context={'text': text})


class Create(View):
    def get(self, request, text):
        return render(request, 'hyperjob/new.html', context={'text': text})
