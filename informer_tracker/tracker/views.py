from django.shortcuts import render
from .models import *

def mainPage(request):
	return render(request,'index.html')

def inputPage(request):
	informerName = request.POST.get('informerName', False)
	beatsName = request.POST.get('beatsName', False)
	informerMobile = request.POST.get('informerMobile', False)
	informerAddress = request.POST.get('informerAddress', False)
	allBeats = Beats.objects.all()
	print allBeats
	if informerName != False:
		beats = Beats.objects.get(beatsName = beatsName)
		informer = Informer(name=informerName,mobile=informerMobile,
							address=informerAddress,beats=beats)
		informer.save()
	return render(request,'input.html',{'allBeats':allBeats})

def viewPage(request):
	beatsName = request.POST.get('beatsName', False)
	allBeats = Beats.objects.all()
	informers = ""
	if beatsName != False:
		beats = Beats.objects.get(beatsName = beatsName)
		informers = Informer.objects.filter(beats=beats)
	return render(request, 'view.html',{'allBeats':allBeats,'informers':informers})
