from django.shortcuts import render

# Create your views here.
def arch(request):
    return render(request,'bin.html')