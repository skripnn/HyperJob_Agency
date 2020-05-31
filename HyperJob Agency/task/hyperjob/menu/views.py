from django.shortcuts import render
from django.views import View


class Menu(View):
    menu_links = {
        'Login': '/login',
        'Sign up': '/signup',
        'Vacancies': '/vacancies',
        'Resumes': '/resumes',
        'Personal profile': '/home'
    }

    def get(self, request):
        return render(request, 'menu/menu.html', context={'menu_links': self.menu_links})
