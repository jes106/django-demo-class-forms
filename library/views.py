from django.contrib import messages
from django.shortcuts import render
from .forms import BookForm

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book saved")
            form = BookForm()
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})