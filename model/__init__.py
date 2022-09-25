from . import datebase
from . import author
from . import books


db = datebase.db

Author = author.Author
AuthorSchema = author.AuthorSchema

Book = books.Book
BookSchema = books.BookSchema

