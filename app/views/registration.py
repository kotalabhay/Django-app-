
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from app.Forms.Registration_forms import RegisterForm , AccountAuthenticationForm
from django.http import HttpResponse, HttpResponseNotFound
from app.models import *
from django.views import View

class UnAuthorized(View):

    def get(self, request):
        template_name = 'base/error_page.html'
        return render(request, template_name, {})

def register(request):
	context = {}
	if request.POST:
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password1')
			account = authenticate(email=email, password=raw_password)
			#login(request, account)
			return redirect('register')
		else:
			#form = RegisterForm()
			context['form'] = form
			return HttpResponseNotFound('<h1>Please Check the followings <ul><li>Username and Email must be Unique</li><li>Password must not be same as Username and size of password must be 8 digit</li></ul></h1>')
	else: #GET request
		form = RegisterForm()
		context['form'] = form
	return render(request, 'register/index.html', context)



def logout_view(request):
	logout(request)
	return redirect('home')



def login_view(request):

	 context = {}

	 user = request.user
	 if user.is_authenticated:
	 	return redirect("dashboard")

	 if request.POST:
	 	form = AccountAuthenticationForm(request.POST)
	 	if form.is_valid():
	 		email = request.POST['email']
	 		password = request.POST['password']
	 		user = authenticate(email=email, password=password)

	 		if user:
	 			login(request, user)
	 			return redirect("dashboard")

	 else:
	 	form = AccountAuthenticationForm()

	 context['login_form'] = form
	 return render(request, 'Login/index.html', context)


