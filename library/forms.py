from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'category', 'price', 'date_released']

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) <= 5:
            raise forms.ValidationError("Book name too short")
        return name