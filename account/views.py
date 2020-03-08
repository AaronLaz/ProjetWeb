from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import *
from blog.models import BlogPost
from account.models import Account
# Create your views here.

# view to register new user
def registration_view(request):
	context = {}
	if request.POST: # if post method
		form = registration_form(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			login(request,account)
			return redirect('homepage')
		else:
			context['registration_form'] = form
	else: # if get method
		form = registration_form()
		context['registration_form'] = form
	return render(request, 'account/register.html',context)				

# view to log out
def logout_view(request):
	logout(request)	
	return redirect('homepage')

# login
def login_view(request):
	context = {}

	user = request.user
	if user.is_authenticated:
		return redirect('homepage')

	if request.POST:
		form = authentication_form(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request,user)
				return redirect('homepage')

	else: # not authenticated/not tried to login
		form = authentication_form()

	context['login_form'] = form
	return render(request,'account/login.html',context)

# account details/edit view
def account_view(request):

	if not request.user.is_authenticated:					
		return redirect('login')

	context = {}
	
	# form to edit email and username
	if request.POST:
		form = update_form(request.POST, instance=request.user) # form requires instance
		if form.is_valid():
			form.initial={
				"email": request.POST['email'],
				"username": request.POST['username'],
			}
			form.save()
			context['success_message'] = "Changes saved successfully"
	else:
		form = update_form(
				initial= {
					"email" : request.user.email,
					"username" : request.user.username,
				}
			)
	context['account_form'] = form

	blog_posts = BlogPost.objects.filter(author=request.user)
	context['blog_posts'] = blog_posts

	return render(request, 'account/account.html',context)				

# when user is not logged in
def must_authenticate_view(request):
	return render(request,'account/must_authenticate.html',{})

# when user does not have required privileges
def unauthorized_view(request):
	return render(request,'account/unauthorized.html',{})	

# admin userlist view
def userlist(request):
	context = {}
	if not request.user.is_admin:
		return redirect("unauthorized")
	else:
		# return all users
		context['users'] = Account.objects.all()
		return render(request,'account/userlist.html',context)		 
