from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    summary = models.TextField(blank=True, null=True)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Librarian(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    hire_date = models.DateField()
    books_managed = models.ManyToManyField(Book, related_name='librarians')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"