from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import NewBookForm, BorrowBookForm

from .models import Book

def home(request):
    data = { 'books': Book.objects.all() }
    return render(request, 'library/home.html', data)

@login_required
def show(request, id):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            if book.borrower == request.user:
                book.borrower = None
                book.save()
                return redirect("library-show", id=id)
            else:
                book.borrower = request.user
                book.save()
                return redirect("library-show", id=id)
    else:
        print("I am not there")
        form = BorrowBookForm(initial={'borrower': request.user})
    data = {
        'book': book,
        'form': form
    }
    return render(request, 'library/show.html', data)
    
def not_found_404(request, exception):
    data = { 'err': exception }
    return render(request, 'library/404.html', data)

def server_error_500(request):
    return render(request, 'library/500.html')

@login_required
def create(request):
    if request.method == 'POST':
        book = NewBookForm(request.POST)
        if book.is_valid():
            id = book.save().id
            return redirect("library-show", id = id)
    else:
        form = NewBookForm()
    data = {'form': form}
    return render(request, 'library/new.html', data)
