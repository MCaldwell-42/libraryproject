import sqlite3
from django.shortcuts import render
from libraryapp.models import Book
from libraryapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Book)
            # conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbnnumber,
                b.author,
                b.YearPublished,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)

            all_books = db_cursor.fetchall()

            # for row in dataset:
            #     book = Book()
            #     book.id = row['id']
            #     book.title = row['title']
            #     book.isbnnumber = row['isbnnumber']
            #     book.author = row['author']
            #     book.YearPublished = row['YearPublished']
            #     book.librarian_id = row['librarian_id']
            #     book.location_id = row['location_id']

            #     all_books.append(book)

        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)