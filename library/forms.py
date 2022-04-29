from django import forms
from .models import Book

class NewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['borrower']
        widgets = {'borrower': forms.HiddenInput()}

