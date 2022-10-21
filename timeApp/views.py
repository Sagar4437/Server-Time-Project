from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def giveTime(request):
    from datetime import datetime
    time = datetime.now().strftime("%H : %M : %S")
    value = f"Hellow Guest... Current Server time is {time}"
    return HttpResponse(value)
