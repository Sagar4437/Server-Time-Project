from django.shortcuts import render

# Create your views here.
def giveTime(request):
    from datetime import datetime
    time = datetime.now().strftime("%H : %M : %S")
    return render(request,'timeApp/index.html',{'time':time})
