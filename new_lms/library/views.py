from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from rest_framework.decorators import api_view
from .models import *


# class LibrarianView(viewsets.ModelViewSet):
#
#     serializer_class = LibrarianSerializer
#     queryset = Librarian.objects.all()
#
# class LibraryView(viewsets.ModelViewSet):
#     serializer_class = LibrarySerializer
#     queryset = Library.objects.all()
#
#
# class BookView(viewsets.ModelViewSet):
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()
#
# class MemberView(viewsets.ModelViewSet):
#     serializer_class = MemberSerializer
#     queryset = Member.objects.all()
#
# class RecordView(viewsets.ModelViewSet):
#     serializer_class = RecordSerializer
#     queryset = Record.objects.all()


@api_view(['GET',])
def api_book_list_view(request):
    book = Book.objects.all()
    if request.method == 'GET':
        serializers = BookSerializer(book, many=True)
    return Response(serializers.data)

@api_view(['GET','PUT'])
def api_book_details_update(request, pk):
    data = {}
    try:
        book = Book.objects.get(book_id=pk)
    except Book.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializers = BookSerializer(book)
    if request.method == 'PUT':
        serializers = BookSerializer(book, many=True)
        if serializers.is_valid():
            serializers.save()
            data['Success'] = 'Put operation completed successfully'
            return Response(data=data)
    return Response(serializers.errors, status.HTTP_404_NOT_FOUND)

@api_view(['POST',])
def api_book_delete_list(request):
    data = {}
    if request.method == 'POST':
        serializers = BookSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            data['Success'] = 'Post operation completed successfully'
            return Response(data=data)
        return Response(serializers.errors, status.HTTP_404_NOT_FOUND)








@api_view(['PUT',])
def api_record_list_view(request):
    record = Record.objects.all()
    if request.method == 'PUT':
        serializers = RecordSerializer(record, many=True)
    return Response(serializers.data)


@api_view(['PUT'])
def api_record_update(request,pk):
    try:
        record = Record.objects.get(record_id=pk)
    except Record.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializers = RecordSerializer(record,data=request.data)
        if serializers.is_valid():
            serializers.save()
            data = {}
            data['Success'] = 'Update Successfull'
            return Response(data=data)

        return Response(serializers.errors, status.HTTP_404_NOT_FOUND)

@api_view(['PUT',])
def api_member_list(request,pk):
    try:
        member = Member.objects.get(member_ID=pk)
    except Member.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializers = MemberSerializer(member,data=request.data)
        if serializers.is_valid():
            serializers.save()
            data = {}
            data['Success'] = 'Put operation completed successfully'
            return Response(data=data)
        return Response(serializers.errors, status.HTTP_404_NOT_FOUND)


@api_view(['DELETE',])
def api_member_delete_list(request,pk):
    try:
        member = Member.objects.get(member_ID=pk)
    except Member.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        data = {}
        operation = member.delete()
        if operation:
            data['Success'] = 'Delete operation completed successfully'
        else:
            data["Failure"] = "Delete Failed"
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


