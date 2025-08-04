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

def candidates(request):
  return render(request, 'candidates.html')

def parties(request):
  return render(request, 'parties.html')

def elections(request):
  return render(request, 'elections.html')

def voters(request):
  return render(request, 'voters.html')

def vote(request):
  return render(request, 'vote.html')

def candidates_list(request):
  return render(request, 'candidates_list.html')

def parties_list(request):
  return render(request, 'parties_list.html')

def elections_list(request):
  return render(request, 'elections_list.html')

def voters_list(request):
  return render(request, 'voters_list.html')

def vote_list(request):
  return render(request, 'vote_list.html')

def result_list(request):
  return render(request, 'result_list.html')

def result(request):
  return render(request, 'result.html')
