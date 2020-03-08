from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage
from myapp.models import *
from account.models import Account
from blog.models import BlogPost
from operator import attrgetter
from blog.views import get_blog_queryset
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

BLOG_POSTS_PER_PAGE = 10

# Create your views here.

def index(request):
	return render(request,'index.html')

def homepage(request):
	context = {}

	query = ""
	if request.GET:
		query = request.GET.get('q','') # get value of query, default is empty
		context['query'] = str(query)

	# Sort all blog posts by latest date
	blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'),reverse=True)
	context['blog_posts'] = blog_posts

	# Page numbers
	page = request.GET.get('page',1) #default number is 1
	blog_posts_pagenum = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)

	try:
		blog_posts = blog_posts_pagenum.page(page)
	except PageNotAnInteger:	
		blog_posts = blog_posts_pagenum.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_pagenum.page(blog_posts_pagenum.num_pages)

	context['blog_posts'] = blog_posts	

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