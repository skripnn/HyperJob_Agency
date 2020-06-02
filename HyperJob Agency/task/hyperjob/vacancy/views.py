from django.shortcuts import render, redirect
from django.views import View
from .models import Vacancy
from django.core.exceptions import PermissionDenied


class AllVacancy(View):
    def get(self, request):
        context = {'list': Vacancy.objects.all(), 'text': 'Vacancies'}
        return render(request, 'hyperjob/all.html', context=context)


class Create(View):
    def get(self, request):
        return render(request, 'hyperjob/new.html', context={'text': 'resume'})

    def post(self, request):
        if not request.user.is_staff:
            raise PermissionDenied

        Vacancy.objects.create(
            description=request.POST['description'],
            author=request.user
        )

        return redirect('/home')
