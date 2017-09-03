from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from forms import LoginForm
from utils import Book



@csrf_protect
def login(request):
	form = LoginForm(request.POST)
	print("login function working")
	if form.is_valid():
		print(form.cleaned_data)
		print(form.cleaned_data['username'], form.cleaned_data['password'])
	#user verification 
	#user registration occurs here
	tmp = Book.Portfolio(form.cleaned_data['username'])
	context = {"portfolio": tmp}
   	return render(request,'portfolio.html',context)





