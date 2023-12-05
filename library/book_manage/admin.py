from django.contrib import admin
from book_manage.models import Book,Patron,Borrow
# Register your models here.
admin.site.register(Book)
admin.site.register(Patron)
admin.site.register(Borrow)