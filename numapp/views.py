from django.shortcuts import render

# Create your views here.



def home(request):
    
    context ={}

    var1 = request.POST.get("num1")
    var2 = request.POST.get("num2")

    if request.method == 'POST':
        sum = int(var1) + int(var2)
        context.update({'result':sum})
    return render(request,'home.html',context)
