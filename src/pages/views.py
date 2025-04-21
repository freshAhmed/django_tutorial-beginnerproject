from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage_view(request,*args,**kwargs):
 
 return render(request,'home.html',{})

def contactpage_view(request,*args,**kwargs):
 my_content={'number':'+5640835743','direction':'trinidad Ramierz 180'}
 return render(request,'contact.html',my_content)