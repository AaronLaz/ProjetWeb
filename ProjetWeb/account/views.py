from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import RegistrationForm

# Create your views here.

def registration_view(request):
	context = {}
	if request.POST: # if post method
		form = RegistrationForm(request.POST)
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
		form = RegistrationForm()
		context['registration_form'] = form
	return render(request, 'account/register.html',context)				