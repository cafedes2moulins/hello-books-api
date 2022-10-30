from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, request, make_response



books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def read_all_books():
    books = Book.query.all()
    book_response = []
    for book in books:
        book_response.append(
            {"id": book.id,
            "title": book.title,
            "description": book.description
            }
        )
    return jsonify(book_response)
 # flask allows us to put functionality for multiple features into a single function
# but it enhances readability and editability if we separate them into their own funcitons
 


# @books_bp.route("/<book_id>", methods=["GET"])
# def get_specific_book(book_id):
#     try:
#         verified_id = int(book_id)
#     except ValueError:
#         return jsonify("Invalid ID: id must be an integer"), 400

#     for book in books:
#         if book.id == book_id:
#             book_dict = {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#             return jsonify(book_dict), 200
#     return jsonify(f"ID not found: book with id '{book_id}' does not exist"), 404





@books_bp.route("", methods = ["POST"])
def add_book():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book '{new_book.title}' successfully created", 201)









#      WHAT IT LOOKS LIKE TO COMBINE FEATURES IN ONE FUNCTION

# @books_bp.route("", methods=["GET", "POST"])
# def handle_books():
#     if request.method == "GET":
#         books = Book.query.all()
#         book_response = []
#         for book in books:
#             book_response.append(
#                 {"id": book.id,
#                 "title": book.title,
#                 "description": book.description
#                 }
#             )
#         return jsonify(books)
#     elif request.method == "POST":
#         request_body = request.get_json()
#         new_book = Book(title=request_body["title"],
#         description=request_body["description"])

#         db.session.add(new_book)
#         db.session.commit

#         return make_response(f"Book '{new_book.title}' successfully created", 201)