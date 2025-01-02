from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def index(request):
    # return render(request,'author/index.html')
    return HttpResponse(render_to_string('demo/index.html'))
