
from django.shortcuts import render, redirect
from .models import BookInfo
from .forms import BookForm, BookEditForm

def register_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'register_book.html', {'form': form})



def edit_book(request, pk):
    book = BookInfo.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookEditForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'pk': pk})



def book_list(request):
    if request.method == 'FILTER':
        books = BookInfo.objects.GET.get(ISBN)
    else:
        books = BookInfo.objects.all()

    context = {'books': books}
    return render(request, 'book_list.html', context)

# def book_list(request):
#     query = request.GET.get('q')
#     if query:
#         books = BookInfo.objects.filter(Q(ISBN__icontains=query))
#     else:
#         books = BookInfo.objects.all()
#     context = {'books': books}
#     return render(request, 'book_list.html', context)



def book_detail(request, pk):
    book = BookInfo.objects.get(pk=pk)
    context = {'book': book}
    return render(request, 'book_detail.html', context)


