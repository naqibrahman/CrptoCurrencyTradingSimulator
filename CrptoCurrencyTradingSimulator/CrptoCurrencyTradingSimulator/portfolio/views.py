from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from forms import LoginForm
from utils import Book
import json



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
	marketList = tmp.getActiveMarkets()
	holdingsJSON = tmp.holdings.to_json()
	holdingsList = json.loads(holdingsJSON)['Quantity']['BTC'] #should probably write a function to find total holdings
	context = {"portfolio": tmp, "marketList": marketList , "marketLength" : len(marketList) , "holdingsList" : holdingsList, 'holdingsLength' :len(tmp.holdings) }
   	return render(request,'portfolio.html',context)





