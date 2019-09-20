from django.conf.urls import url, include
from django.urls import path
from .views import *

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^books$', book_list, name='books'),
    path('books/<int:book_id>/', book_details, name='book'),
    url(r'^librarians$', list_librarians, name='librarians'),
    path('librarians/<int:librarian_id>/', librarian_details, name='librarian'),
    url(r'^libraries$', library_list, name='libraries'),
    path('libraries/<int:library_id>/', library_details, name='library'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^books/form$', book_form, name='book_form'),
    url(r'^books/(?P<book_id>[0-9]+)/form$', book_edit_form, name='book_edit_form'),
    url(r'^libraries/form$', library_form, name='library_form'),
]