from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReviewForm

# Create your views here.
def review(request):
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('thankyou')
    else:
        form=ReviewForm()
    return render(request,'reviews/review.html',{
        'form':form
    })
