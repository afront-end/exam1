from django.db import models

class UserModel(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField()

    def __str__(self):
        return self.email

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Author(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    photo = models.ImageField(upload_to='author_photos/', null=True, blank=True)
    bio = models.TextField()

class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='pulisher_photos/',null=True,blank=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    pages = models.IntegerField()
    cover = models.ImageField(upload_to='book_photos/',null=True,blank=True)
    description = models.TextField()