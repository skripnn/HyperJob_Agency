from django.shortcuts import render
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
