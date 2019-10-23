from django.contrib import admin
from django import forms
from django.forms import ModelForm
from .models import *

class Libraryadmin(admin.ModelAdmin):
    list_display = ('library_id','library_name','location','librarian')


admin.site.register(Library, Libraryadmin)

# class BookAdminForm(forms.ModelForm):
#     def __init__(self,*args,**kwargs):
#         super(BookAdminForm,self).__init__(*args,**kwargs)
#
#     def clean(self):
#         borrowed_book = self.cleaned_data.get('borrowed_book')
#         is_returned = self.cleaned_data.get('returned')
#         total_no_books = self.cleaned_data.get('borrowed_book')
#         if not is_returned:
#             if borrowed_book.stock == 0 and :
#                 raise forms.ValidationError("book is out of stock", code='invalid')
#             return self.cleaned_data
#
#     def save(self, commit=True):
#         return super(BookAdminForm, self).save(commit=commit)


class Bookadmin(admin.ModelAdmin):
    list_display = ('book_id', 'book_name', 'book_price', 'ISBN', 'available', 'author', 'total_no_books', 'stock',)
    search_fields = ['book_name']
    list_filter = ('available',)
    ordering = ('book_name',)

admin.site.register(Book, Bookadmin)


class Librarianadmin(admin.ModelAdmin):
    list_display = ('library_ID','name', 'email',)


admin.site.register(Librarian, Librarianadmin)


class Memberadmin(admin.ModelAdmin):
    list_display = ('member_ID','member_name','member_email','member_phone',)


admin.site.register(Member, Memberadmin)

class Recordadmin(admin.ModelAdmin):
    list_display = ('record_id', 'issued_librarian', 'book_borrowed', 'issued_to_member', 'borrow_date', 'return_date', 'returned', 'actual_return','is_due',)

admin.site.register(Record, Recordadmin)