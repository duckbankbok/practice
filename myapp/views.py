from django.shortcuts import render, get_object_or_404, redirect
from .models import visit
from django.utils import timezone

# Create your views here.

def home(request):
    visitors_book = visit.objects
    return render(request, 'home.html', {'visitors' : visitors_book})

def about(request):
    return render(request, 'about.html')

def detail(request, book_id):
    book_detail = get_object_or_404(visit, pk=book_id)
    return render(request, 'detail.html', {'book' : book_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    book = visit()
    book.visitor = request.GET['visitor']
    book.body = request.GET['body']
    book.pub_date = timezone.datetime.now()
    book.save()
    return redirect('/detail/'+str(book.id))

def delete(request, book_id):
    book = visit.objects.get(pk=book_id)
    book.delete()
    return redirect('/')

def update(request, book_id):
    return render(request, 'update.html', {'book':book_id})

def update_final(request, book_id):
    book = visit.objects.get(pk=book_id)
    book.visitor = request.GET['visitor']   
    book.body = request.GET['body']
    book.pub_date = timezone.datetime.now()
    book.save()
    return redirect('/detail/'+str(book.id)) 