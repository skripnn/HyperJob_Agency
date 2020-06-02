from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View
from .models import Resume


class AllResumes(View):
    def get(self, request):
        context = {'list': Resume.objects.all(), 'text': 'Resumes'}
        return render(request, 'hyperjob/all.html', context=context)


class Create(View):
    def get(self, request):
        return render(request, 'hyperjob/new.html', context={'text': 'resume'})

    def post(self, request):
        if request.user.is_staff:
            raise PermissionDenied

        Resume.objects.create(
            description=request.POST['description'],
            author=request.user
        )

        return redirect('/home')
