from rest_framework import serializers
from .models import *


class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = ("name",)


class LibrarySerializer(serializers.ModelSerializer):
    librarian = LibrarianSerializer()

    class Meta:
        model = Library
        fields = ("library_name", "location", "librarian")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("book_id", "book_name", "author")


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("member_name", "member_email")


class RecordSerializer(serializers.ModelSerializer):
    issued_librarian = LibrarianSerializer()
    issued_to_member = MemberSerializer()
    book_borrowed = BookSerializer()

    class Meta:
        model = Record
        fields = (
            "issued_librarian",
            "book_borrowed",
            "issued_to_member",
            "borrow_date",
            "return_date",
            "returned",
            "actual_return",
        )
