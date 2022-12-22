from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404

def website(request):
    context={}
    return render(request, 'website-home.html', context)
