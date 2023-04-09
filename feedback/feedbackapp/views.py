from django.shortcuts import render
from feedbackapp.forms import feedbackform
from django.http import HttpResponse
from feedbackapp.models import feedbackmodel
def feedbackview(request):
    if request.method=='POST':
        print("feedback submitted successfully")
        fform=feedbackform(request.POST)
        if fform.is_valid():
            name1=request.POST.get("name")
            tutor1=request.POST.get("tutorname")
            feed1=request.POST.get("feedback12")
            data=feedbackmodel(name=name1,tutorname=tutor1,feedback12=feed1)
            data.save()
        f1=feedbackform()
        return HttpResponse("your feedback submitted successfully")
    f1=feedbackform()
    return render(request,'feed.html',context={'fform':f1})    
