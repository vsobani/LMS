from django.urls import path, include
from .views import *

# from .views import api_book_list_view,api_book_details_view,api_book_details_update,\
#     api_book_delete_list ,\
# api_member_list_view, api_member_details_view,api_member_details_create,\
#     api_member_details_update, api_member_delete_list,\
# api_record_list_view,api_record_details_view,api_record_details_create,\
#     api_record_details_update,api_record_delete_list
# api_librarian_list_view,api_librarian_details_view,api_librarian_details_create,\
#     api_librarian_details_update,api_librarian_delete_list

from rest_framework import routers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# router = routers.DefaultRouter()
# router.register('book', views.BookView)
# router.register('library', views.LibraryView)
# router.register('librarian', views.LibrarianView)
# router.register('member', views.MemberView)
# router.register('record', views.RecordView)


app_name = "library"

# urlpatterns = [
#  # path('', include(router.urls)),
#     # path('books/', api_book_list_view, name='book'),
#     # path('books/<pk>/', api_book_details_update, name='book-details'),
#     # path('books/<pk>/update/', api_book_details_update, name='book'),
#     # path('books/post',api_book_delete_list,name= 'book-delete'),
#     # path('records/', api_record_list_view, name='record'),
#     # path('records/<pk>/update', api_record_update, name='record'),
#     # path('member/<pk>/update', api_member_list, name='member'),
#     # path('member/<pk>/delete', api_member_delete_list,name='member-delete')
# ]

# urlpatterns =  [
#     path('books', BookList.as_view(), name='book-list'),
# ]


urlpatterns = [
    path("books/", api_book_list_view, name="book-list-view"),
    path("books/<int:pk>/", api_book_details_view, name="book-details-view"),
    path("books/create/", api_book_details_create, name="book-details-create"),
    path("books/<int:pk>/update/", api_book_details_update, name="book-details-update"),
    path("books/<int:pk>/delete/", api_book_delete_list, name="book-details-delete"),
    path("members/", api_member_list_view, name="member-list-view"),
    path("members/<int:pk>/", api_member_details_view, name="member-details-view"),
    path("members/create/", api_member_details_create, name="member-details-create"),
    path("members/<int:pk>/update/",api_member_details_update,name="member-details-update"),
    path("members/<int:pk>/delete/", api_member_delete_list, name="member-details-delete"),
    path("records/", api_record_list_view, name="record-list-view"),
    path("records/<int:pk>/", api_record_details_view, name="record-details-view"),
    path("records/create/", api_record_details_create, name="record-details-create"),
    path("records/<int:pk>/update",api_record_details_update,name="record-details-update"),
    path("records/<int:pk>/delete", api_record_delete_list, name="record-details-delete"),
    path("library/", api_library_list_view, name="library-list-view"),
    path("library/<int:pk>/", api_library_details_view, name="library-details-view"),
    path("library/create/", api_library_details_create, name="library-details-create"),
    path("library/<int:pk>/update/",api_library_details_update,name="library-details-update"),
    path("library/<int:pk>/delete/", api_library_delete_list, name="library-delete-list"),
    path("librarian/", api_librarian_list_view, name="library-list-view"),
    path("librarian/<int:pk>/", api_librarian_details_view, name="library-details-view"),
    path("librarian/create/", api_librarian_details_create, name="library-details-create"),
    path("librarian/<int:pk>/update/",api_librarian_details_update,name="library-details-update"),
    path("librarian/<int:pk>/delete/",api_librarian_delete_list,name="library-delete-list"),
    path("booksgeneric/get/", BookListView.as_view(), name="book-list"),
    path("booksgeneric/get/<int:pk>/", BookListView.as_view(), name="book-update"),
    path("recordsgeneric/get/",RecordListView.as_view(),name="record-list"),
    path("recordsgeneric/get/<int:pk>/",RecordListView.as_view(),name='"record-update'),
]
