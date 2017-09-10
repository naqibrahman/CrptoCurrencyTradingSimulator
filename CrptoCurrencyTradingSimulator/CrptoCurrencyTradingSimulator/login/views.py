from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

@csrf_protect
def landingPage(request):
	print("landingPage()")
	return render(request,'login.html')
