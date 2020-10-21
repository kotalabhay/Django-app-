from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404


def index(request):
    template_name = 'Dashboard/index.html'
    return render(request, template_name, {})
