from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from random import randint

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Book(BaseModel):
    title: str
    author: str
    read: bool

BOOKS = [
    {
        'id': randint(1, 1000000),
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': randint(1, 1000000),
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': randint(1, 1000000),
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

@app.get('/ping')
def ping_pong():
    return 'pong!'

@app.get('/books')
def all_books():
    return jsonable_encoder({
        'status': 'success',
        'books': BOOKS
    })

@app.post('/books')
def save_books(book: Book):
    response_object = {'status': 'success'}
    BOOKS.append({
        'id': randint(1, 1000000),
        'title': book.title,
        'author': book.author,
        'read': book.read
    })
    response_object['message'] = 'Book added!'
    return jsonable_encoder(response_object)

@app.put('/books/{book_id}')
def update_book(book_id: int, book: Book):
    book_for_update=[ book for book in BOOKS if book['id'] == book_id ][0]
    response_object = {'status': 'success'}
    book_for_update['title']=book.title
    book_for_update['author']=book.author
    book_for_update['read']=book.read
    response_object['message'] = 'Book updated!'
    return response_object

@app.delete('/books/{book_id}')
def delete_book(book_id: int):
    response_object = {'status': 'success'}
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)

    response_object['message'] = 'Book removed!'
    return response_object
