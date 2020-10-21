from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from project_master.Forms.Project_master_forms import *
from django.http import HttpResponse, HttpResponseNotFound
from project_master.models import *
from django.views import View
from django.forms.models import modelformset_factory


# Create your views here.
#def create_project(request):
	#context = {}
	#if request.POST:
		#form = Project_MasterForm(request.POST)
		#if form.is_valid():
			#form.save()
				#login(request, account)
			#return redirect('home')
		#else:
			#form = RegisterForm()
		#	context['form'] = form
			#return HttpResponseNotFound('<h1>Please Check the followings <ul><li>Username and Email must be Unique</li><li>Password must not be same as Username and size of password must be 8 digit</li></ul></h1>')
#	else: #GET request
		#form = Project_MasterForm()
		#context['form'] = form
	#return render(request, 'project_create/index.html', context)

#Project_MasterFormset





def create_project(request):
	template_name = 'project_create/index.html'
	#form = Project_MasterForm()
	#RelatedFormset = modelformset_factory(Project_Master, extra=1)
	#heading_message = 'Model Formset Demo'
	if request.method == 'GET':
		Project_Masterform = Project_MasterForm(request.GET or None)
		formset = Project_MasterFormset(queryset=Tc_Details.objects.none())
	elif request.method == 'POST':
		Project_Masterform = Project_MasterForm(request.POST, request.FILES or None)
		formset = Project_MasterFormset(request.POST)
		Project_Masterform.instance.autor = request.user
		#formset.instance.autor = request.user
		if Project_Masterform.is_valid() and formset.is_valid():
			tc=Project_Masterform.save()
			for form in formset:
				project= form.save(commit=False)
				#project.id=request.id
				project.tc=tc
				project.save()
			return redirect('dashboard')
	return render(request, template_name, {
		'form':Project_Masterform,
		'formset': formset,
		#'heading': heading_message,
	})