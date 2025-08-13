from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler -> view function

def hello(request):
    # Pull data from db
    # Process data
    # send emails etc
   
    return render(request,'hello.html',{'name':'UK'}) 