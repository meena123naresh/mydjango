from django.shortcuts import render
from formsapp.forms import contactform
from django.http import HttpResponse
from formsapp.models import contact
def contactview(request):
    if request.method=='POST':
        print("you submitted")
        cform= contactform(request.POST)
        if cform.is_valid():
            name1=request.POST.get("name")
            email1=request.POST.get("email")
            phone1=request.POST.get("phone")
            city1=request.POST.get("city")
            data=contact(name=name1,email=email1,phone=phone1,city=city1)
            data.save()
        a1=contactform()
        return HttpResponse("form submitted and data saved")
    a1=contactform()
    return render(request,'home.html',context={'cform':a1})

# Create your views here.
