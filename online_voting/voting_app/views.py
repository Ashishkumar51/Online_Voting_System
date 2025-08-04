from django.shortcuts import render
from django.http import HttpResponse

def dahboard(request):
  return render(request, 'Dashboard.html')

def form(request):
  return render(request, 'form.html')

def overview(request):
  return render(request, 'overview.html')

def login(request):
  return render(request, 'login.html')

def  form(request):
  return render(request, 'form.html')


# Create your views here.
