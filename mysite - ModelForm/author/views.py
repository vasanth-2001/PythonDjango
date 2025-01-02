from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Book
from django.http import Http404

def index(request):
    # return render(request,'author/index.html')
    book=Book.objects.all()
    return render(request,'author/index.html',{
        'book_collection':book
    })

def bookdetail(request,id):
    # try:
    #     book=Book.objects.get(pk=id)
    # except:
    #     raise Http404()

    books=get_object_or_404(Book,pk=id)
    return render(request,'author/detail.html',{
        'title1':books.title,
        'rating':books.rating
        # 'book_collections':books

    })