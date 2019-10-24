from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializer import *
from rest_framework.decorators import api_view
from .models import *
from rest_framework import generics


class LibrarianView(viewsets.ModelViewSet):

    serializer_class = LibrarianSerializer
    queryset = Librarian.objects.all()

class LibraryView(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()


class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class RecordView(viewsets.ModelViewSet):
    serializer_class = RecordSerializer
    queryset = Record.objects.all()


@ api_view(['GET'])
def api_book_list_view(request):
    book = Book.objects.all()
    if request.method == 'GET':
        serializer = BookSerializer(book,many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def api_book_details_view(request,pk):
    try:
        book = Book.objects.get(book_id=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

@api_view(['POST'])
def api_book_details_create(request):
    data = {}
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['Success'] = 'Create/Post operation successful!'
            return Response(data=data)
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

@ api_view(['PUT'])
def api_book_details_update(request, pk):
    try:
        book = Book.objects.get(book_id=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update/Put operation successful'
            return Response(data=data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE',])
def api_book_delete_list(request,pk):
    try:
        book = Book.objects.get(book_id=pk)
    except Book.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        data = {}
        operation = book.delete()
        if operation:
            data['Success'] = 'Delete operation completed successfully'
        else:
            data["Failure"] = "Delete Failed"
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)



"""This is for the member serilizer class"""


@ api_view(['GET'])
def api_member_list_view(request):
    member = Member.objects.all()
    if request.method == 'GET':
        serializer = MemberSerializer(member, many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def api_member_details_view(request,pk):
    try:
        member = Member.objects.get(member_ID=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MemberSerializer(member)
        return Response(serializer.data)


@api_view(['POST'])
def api_member_details_create(request):
    data = {}
    if request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['Success'] = 'Create/Post operation successful!'
            return Response(data=data)
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

@ api_view(['PUT'])
def api_member_details_update(request, pk):
    try:
        member = Member.objects.get(member_ID=pk)
    except Member.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = MemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update/Put operation successful'
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


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


"""This is for the record serializer class"""


@ api_view(['GET'])
def api_record_list_view(request):
    record = Record.objects.all()
    if request.method == 'GET':
        serializer = RecordSerializer(record, many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def api_record_details_view(request,pk):
    try:
        record = Record.objects.get(record_id=pk)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RecordSerializer(record)
        return Response(serializer.data)


@api_view(['POST'])
def api_record_details_create(request):
    data = {}
    if request.method == 'POST':
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['Success'] = 'Create/Post operation successful!'
            return Response(data=data)
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

@ api_view(['PUT'])
def api_record_details_update(request, pk):
    try:
        record = Record.objects.get(record_id=pk)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = RecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update/Put operation successful'
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE',])
def api_record_delete_list(request,pk):
    try:
        record = Record.objects.get(record_id=pk)
    except Record.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        data = {}
        operation = record.delete()
        if operation:
            data['Success'] = 'Delete operation completed successfully'
        else:
            data["Failure"] = "Delete Failed"
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


"""This is for the library serilizer class"""


@ api_view(['GET'])
def api_library_list_view(request):
    library = Library.objects.all()
    if request.method == 'GET':
        serializer = LibrarySerializer(library, many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def api_library_details_view(request,pk):
    try:
        library = Library.objects.get(library_id=pk)
    except Library.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LibrarySerializer(library)
        return Response(serializer.data)


@api_view(['POST'])
def api_library_details_create(request):
    data = {}
    if request.method == 'POST':
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['Success'] = 'Create/Post operation successful!'
            return Response(data=data)
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

@ api_view(['PUT'])
def api_library_details_update(request, pk):
    try:
        library = Library.objects.get(library_id=pk)
    except Library.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = LibrarySerializer(library, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update/Put operation successful'
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE',])
def api_library_delete_list(request,pk):
    try:
        library = Library.objects.get(library_id=pk)
    except Library.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        data = {}
        operation = library.delete()
        if operation:
            data['Success'] = 'Delete operation completed successfully'
        else:
            data["Failure"] = "Delete Failed"
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)


"""This is for the librarian serilizer class"""


@ api_view(['GET'])
def api_librarian_list_view(request):
    librarian = Librarian.objects.all()
    if request.method == 'GET':
        serializer = LibrarianSerializer(librarian, many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def api_librarian_details_view(request,pk):
    try:
        librarian = Librarian.objects.get(library_ID=pk)
    except Librarian.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LibrarianSerializer(librarian)
        return Response(serializer.data)


@api_view(['POST'])
def api_librarian_details_create(request):
    data = {}
    if request.method == 'POST':
        serializer = LibrarianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['Success'] = 'Create/Post operation successful!'
            return Response(data=data)
        return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

@ api_view(['PUT'])
def api_librarian_details_update(request, pk):
    try:
        librarian = Librarian.objects.get(library_ID=pk)
    except Librarian.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        serializer = LibrarianSerializer(librarian, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {}
            data['success'] = 'Update/Put operation successful'
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE',])
def api_librarian_delete_list(request,pk):
    try:
        librarian = Librarian.objects.get(library_ID=pk)
    except Librarian.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        data = {}
        operation = librarian.delete()
        if operation:
            data['Success'] = 'Delete operation completed successfully'
        else:
            data["Failure"] = "Delete Failed"
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(status.HTTP_405_METHOD_NOT_ALLOWED)






# class BookList(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def list(self, request):
#         queryset = self.get_queryset()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
#
