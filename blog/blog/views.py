from django.shortcuts import render


def home(request):
    context = dict()
    return render(request,'home.html',context=context)