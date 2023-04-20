from django.shortcuts import render
#from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def django_form(request):
    form=NameForm()
    d={'form':form}
    
    return render(request,'django_form.html',d)