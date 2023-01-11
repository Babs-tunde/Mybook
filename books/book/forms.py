from django import forms
from .models import BookInfo

class BookForm(forms.ModelForm):
    class Meta:
        model = BookInfo
        fields = ['ISBN', 'book_title', 'cost_price', 'author', 'author_origin', 'genre', 'published_date', 'date_received', 'number_of_pages']


class BookEditForm(forms.ModelForm):
    class Meta:
        model = BookInfo
        fields = ['ISBN', 'book_title', 'cost_price', 'author', 'author_origin', 'genre', 'published_date', 'date_received', 'number_of_pages']