from django.shortcuts import render,get_object_or_404,redirect
from .models import *

# def header(request):
#     user_id = request.session.get('user_id')
#     if not user_id:
#         return redirect('login')
#     ans = {'user': UserModel.objects.get(id=user_id)}
#     return render(request,'header.html',ans)

# Authentication
def register_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if UserModel.objects.filter(email=email).first():
            return render(request,'registration/register.html',{'error':'This email already exists!'})
        UserModel.objects.create(
            fullname=fullname,
            email=email,
            password=password
        )
        return redirect('login')
        
    return render(request, 'registration/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = UserModel.objects.filter(email=email, password=password).first()

        if user:
            request.session['user_id'] = user.id
            return redirect('/')
        else:
            return render(request, 'registration/login.html', {'error': 'Error email or password'})
            
    return render(request, 'registration/login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')

def forgot_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_pass = request.POST.get('password')
        user = UserModel.objects.filter(email=email).first()
        
        if user:
            user.password=new_pass
            user.save()
            return redirect('login')
        else:
            return render(request, 'registration/forgot_password.html', {'error': "We haven't such email"})
            
    return render(request, 'registration/forgot_password.html')

def change_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    if request.method == 'POST':
        old_pass = request.POST.get('old_pass')
        new_pass = request.POST.get('new_pass')
        user = UserModel.objects.filter(id=user_id,password=old_pass).first()
        if user:
            user.password = new_pass
            user.save()
            return redirect('/')
        else:
            return render(request,'registration/change_password.html',{'error':'Current password not true !'})

    return render(request, 'registration/change_password.html')



def base(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    return render(request,'base.html')

# Category CRUD
def categories(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    ans = {'categories': Category.objects.all()}
    return render(request,'categories/categories.html',ans)

def categories_create(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    if request.method == 'POST':
        Category.objects.create(
            name = request.POST.get('name'),
            description = request.POST.get('description')
        )
        return redirect('categories')
    return render(request,'categories/categ_create_or_update.html')

def categories_update(request, pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    item = get_object_or_404(Category,id=pk)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.save()
        return redirect('categories')
    return render(request,'categories/categ_create_or_update.html',{'category':item})

def categories_delete(request, pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    item = get_object_or_404(Category,id=pk)
    item.delete()
    return redirect('categories')

def categories_detail(request, pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    item = get_object_or_404(Category,id=pk)
    return render(request,'categories/category.html',{'category':item})
    

# Author CRUD
def authors(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    items = Author.objects.all()
    return render(request, 'authors/authors.html', {'authors': items})

def authors_detail(request, pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    item = get_object_or_404(Author, id=pk)
    return render(request, 'authors/author.html', {'author': item})

def authors_create(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
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
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
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
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    item = get_object_or_404(Author, id=pk)
    item.delete()
    return redirect('authors')

# Publisher CRUD
def publishers(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    ans = {'publishers': Publisher.objects.all()}
    return render(request,'publishers/publishers.html',ans)

def publishers_detail(request, pk):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    item = get_object_or_404(Publisher,id=pk)
    return render(request,'publishers/publisher.html',{'publisher':item})

def publishers_create(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
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
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
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
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    item = get_object_or_404(Publisher,id=pk)
    item.delete()
    return redirect('publishers')

# Book CRUD
def books(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
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
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    item = get_object_or_404(Book,id=pk)
    return render(request,'books/book.html',{'book':item})

def books_create(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
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
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
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
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    item = get_object_or_404(Book,id=pk)
    item.delete()
    return redirect('books')