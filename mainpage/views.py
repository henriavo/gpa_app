from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context = {'quote': "hello from chicago!"}
	return render(request, 'mainpage/index.html', context)