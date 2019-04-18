from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Job

def indexPortifolio(request):
    jobs = Job.objects.all()
    return render(request,'portifolio/index.html', {'jobs':jobs})