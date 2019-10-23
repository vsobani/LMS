from rest_framework import serializers
from .models import *


class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = ('library_ID','name', 'email', )


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ('library_id', 'library_name', 'location', 'librarian')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_id', 'book_name', 'book_price', 'ISBN', 'available','author','total_no_books', 'stock')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('member_ID', 'member_name', 'member_email', 'member_phone')


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('record_id','issued_librarian', 'book_borrowed','issued_to_member','borrow_date', 'return_date','returned','actual_return')
