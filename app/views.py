from django.shortcuts import render,get_object_or_404,redirect
from .models import *

def base(request):
    return render(request,'base.html')

# Category CRUD
def categories(request):
    ans = {'categories': Category.objects.all()}
    return render(request,'categories/categories.html',ans)

def categories_create(request):
    if request.method == 'POST':
        Category.objects.create(
            name = request.POST.get('name'),
            description = request.POST.get('description')
        )
        return redirect('categories')
    return render(request,'categories/categ_create_or_update.html')

def categories_update(request, pk):
    item = get_object_or_404(Category,id=pk)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.save()
        return redirect('categories')
    return render(request,'categories/categ_create_or_update.html',{'category':item})

def categories_delete(request, pk):
    item = get_object_or_404(Category,id=pk)
    item.delete()
    return redirect('categories')

def categories_detail(request, pk):
    item = get_object_or_404(Category,id=pk)
    return render(request,'categories/category.html',{'category':item})
    

# Author CRUD
def authors(request):
    items = Author.objects.all()
    return render(request, 'authors/authors.html', {'authors': items})

def authors_detail(request, pk):
    item = get_object_or_404(Author, id=pk)
    return render(request, 'authors/author.html', {'author': item})

def authors_create(request):
    if request.method == 'POST':
        Author.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            photo=request.FILES.get('photo'),
            bio=request.POST.get('bio')
        )
        return redirect('authors')
    return render(request, 'authors/author_create_or_update.html')

def authors_update(request, pk):
    item = get_object_or_404(Author, id=pk)
    if request.method == 'POST':
        item.full_name = request.POST.get('full_name')
        item.email = request.POST.get('email')
        item.bio = request.POST.get('bio')
        if request.FILES.get('photo'):
            item.photo = request.FILES.get('photo')
        item.save()
        return redirect('authors')
    return render(request, 'authors/author_create_or_update.html', {'author': item})

def authors_delete(request, pk):
    item = get_object_or_404(Author, id=pk)
    item.delete()
    return redirect('authors')

# Publisher CRUD
def publishers(request):
    ans = {'publishers': Publisher.objects.all()}
    return render(request,'publishers/publishers.html',ans)

def publishers_detail(request, pk):
    item = get_object_or_404(Publisher,id=pk)
    return render(request,'publishers/publisher.html',{'publisher':item})

def publishers_create(request):
    if request.method == 'POST':
        Publisher.objects.create(
            name = request.POST.get('name'),
            address = request.POST.get('address'),
            phone = request.POST.get('phone'),
            logo = request.FILES.get('logo')
        )
        return redirect('publishers')
    return render(request,'publishers/pub_create_or_update.html')

def publishers_update(request, pk):
    item = get_object_or_404(Publisher,id=pk)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.address = request.POST.get('address')
        item.phone = request.POST.get('phone')
        if request.FILES.get('logo'):
            item.logo = request.FILES.get('logo')
        item.save()
        return redirect('publishers')
    return render(request,'publishers/pub_create_or_update.html',{'publisher':item})

def publishers_delete(request, pk):
    item = get_object_or_404(Publisher,id=pk)
    item.delete()
    return redirect('publishers')

# Book CRUD
def books(request):
    all_books = Book.objects.all()
    categories = Category.objects.all()

    search = request.GET.get('search', '')
    cat = request.GET.get('category', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')

    if search:
        all_books = all_books.filter(title__icontains=search)
    if cat:
        all_books = all_books.filter(category=cat)
    if min_price:
        all_books = all_books.filter(price__gte=min_price)
    if max_price:
        all_books = all_books.filter(price__lte=max_price)

    ans = {
        'books': all_books,
        'categories': categories,
        'search': search,
        'cat2': cat,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'books/books.html', ans)

def books_detail(request, pk):
    item = get_object_or_404(Book,id=pk)
    return render(request,'books/book.html',{'book':item})

def books_create(request):
    if request.method == 'POST':
        Book.objects.create(
            title = request.POST.get('title'),
            author = get_object_or_404(Author,id=request.POST.get('author')),
            publisher = get_object_or_404(Publisher,id=request.POST.get('publisher')),
            category = get_object_or_404(Category,id=request.POST.get('category')),
            price = request.POST.get('price'),
            pages = request.POST.get('pages'),
            cover = request.FILES.get('cover'),
            description = request.POST.get('description')
        )
        return redirect('books')
    choices = {
        'authors': Author.objects.all(),
        'publishers': Publisher.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request,'books/book_create_or_update.html',choices)

def books_update(request, pk):
    item = get_object_or_404(Book,id=pk)
    if request.method == 'POST':
        item.title = request.POST.get('title')
        item.author = get_object_or_404(Author,id=request.POST.get('author'))
        item.publisher = get_object_or_404(Publisher,id=request.POST.get('publisher'))
        item.category = get_object_or_404(Category,id=request.POST.get('category'))
        item.price = request.POST.get('price')
        item.pages = request.POST.get('pages')
        if request.FILES.get('cover'):
            item.cover = request.FILES.get('cover')
        item.save()
        return redirect('books')
    choices = {
        'authors': Author.objects.all(),
        'publishers': Publisher.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request,'books/book_create_or_update.html', {'book': item, 'choices': choices})

def books_delete(request, pk):
    item = get_object_or_404(Book,id=pk)
    item.delete()
    return redirect('books')