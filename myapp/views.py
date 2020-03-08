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
import random

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

def scramble(request):
	return render(request,'scramble.html')	

def scrambler(request, type):
	context ={}
	moves_2 = ["L", "L2", "L'",
	"R", "R2", "R'",
	"F", "F2", "F'",
	"B", "B2", "B'",
	"U", "U2", "U'",
	"D", "D2", "D'"]
	moves_3 = ["L", "L2", "L'",
	"R", "R2", "R'",
	"F", "F2", "F'",
	"B", "B2", "B'",
	"U", "U2", "U'",
	"D", "D2", "D'"]

	moves_4 = ["L", "L2", "L'",
	"R", "R2", "R'",
	"F", "F2", "F'",
	"B", "B2", "B'",
	"U", "U2", "U'",
	"D", "D2", "D'",
	"f","f2","f'",
	"b","b2","b'",
	"u","u2","u'",
	"d","d2","d'",
	"r","r2","r'",
	"l","l2","l'",
	]

	moves_5 = ["L", "L2", "L'",
	"R", "R2", "R'",
	"F", "F2", "F'",
	"B", "B2", "B'",
	"U", "U2", "U'",
	"D", "D2", "D'",
	"f","f2","f'",
	"b","b2","b'",
	"u","u2","u'",
	"d","d2","d'",
	"r","r2","r'",
	"l","l2","l'",
	"M","M2","M'",
	"E","E2","E'",
	"S","S2","S'",
	]                   

	scramble=""
	puzzle = Puzzle.objects.get(puzzleType=type)	 

	list_scrambles = Scramble.objects.all().filter(scrambleType=puzzle)
	if list_scrambles.count()<15:
		if type==2:
			strtype="2"
			for i in range(15):
				scramble = scramble + " " + random.choice(moves_2)
		elif type==4:
			strtype="4"
			for i in range(15):
				scramble = scramble + " " + random.choice(moves_4)
		elif type==5:
			strtype="5"
			for i in range(15):
				scramble = scramble + " " + random.choice(moves_5)
		else: # default is 3x3
			strtype="3"
			for i in range(15):
				scramble = scramble + " " + random.choice(moves_3)
	

		newscramble = Scramble(scrambleType=puzzle,scramble=scramble)
		context['scramble'] = newscramble
		newscramble.save()
	else:
		context['scramble'] = random.choice(list_scrambles)				

	return render(request,'scramble.html',context)		

def faq(request):
	return render(request,'faq.html')

def about(request):
	return render(request,'about.html')	

def blog(request):
	return render(request,'blog.html')	