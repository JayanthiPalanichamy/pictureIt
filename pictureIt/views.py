from django.shortcuts import render,redirect
from .models import User
from .forms import *
def signup(request):
    context={}
    return render(request,'sign-up.html',context)
def index(request):
    context={}
    return render(request,'index.html',context)
def  ajaxsignup(request):
	ajax=AjaxSignUp(request.POST)
	context={'ajax_output':ajax.ajax_output()}
	return render(request,'ajax.html',context)
def  ajaxlogin(request):
	ajax=AjaxLogin(request.POST)
	logged_in_user,ajax_output=ajax.validate()
	if logged_in_user !=None:
		login(request,logged_in_user)
	context={'ajax_output':ajax.ajax_output()}
	return render(request,'ajax.html',context)