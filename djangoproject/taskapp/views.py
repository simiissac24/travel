from django.http import HttpResponse
from django.shortcuts import render
from .import models
from .models import place



# Create your views here.



def contact(request):
   baby=place.objects.all()

   return render(request,'index.html',{'outcome':baby})

#def calculate(request):
   # x = int(request.GET['num1'])
   # y = int(request.GET['num2'])

   # add_result = x + y
   # mul_result = x * y
   # div_result = x / y
   # sub_result = x - y

    #return render(request, 'result.html', {
      #  'num1': x,
      #  'num2': y,
      #  'add_result': add_result,
       # 'mul_result': mul_result,
        #'div_result': div_result,
       # 'sub_result': sub_result,
    #})

#def details(request):
    #return HttpResponse("please read the details")
#def thanks(request):
    #return render(request,'thanks.html')
