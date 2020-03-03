from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage
from myapp.models import *

# Create your views here.

def index(request):
	return render(request,'index.html')

def homepage(request):
	context = {}
	context['some_string'] = "Welcome user!"
	return render(request,'homepage.html',context)	

def timer(request):
	return render(request,'timer.html')	

def faq(request):
	return render(request,'faq.html')

def about(request):
	return render(request,'about.html')	

def contact(request):
	return render(request,'contact.html')	

def blog(request):
	return render(request,'blog.html')	