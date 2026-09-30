from django.shorcuts import render, redirect
from .forms import BookForm

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Book saved")
        else:
            form = BookForm()
        return render(request, 'library/add_book.html', {'form': form})