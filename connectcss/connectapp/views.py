from django.shortcuts import render
from django.http import HttpResponse
def ok(request):
    return render(request,'ok.html')
