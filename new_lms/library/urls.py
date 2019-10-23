
from django.urls import path ,include
from . import views
from .views import api_member_list,api_record_update,api_book_details_update,\
    api_book_list_view,api_record_list_view,api_member_delete_list,\
    api_book_delete_list

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



app_name = 'library'

urlpatterns = [
 # path('', include(router.urls)),
    path('books/', api_book_list_view, name='book'),
    path('books/<pk>/', api_book_details_update, name='book-details'),
    path('books/<pk>/update/', api_book_details_update, name='book'),
    path('books/post',api_book_delete_list,name= 'book-delete'),
    path('records/', api_record_list_view, name='record'),
    path('records/<pk>/update', api_record_update, name='record'),
    path('member/<pk>/update', api_member_list, name='member'),
    path('member/<pk>/delete', api_member_delete_list,name='member-delete')
]
