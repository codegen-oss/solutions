from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock Data
books = [
    {"id": 1, "title": "Book One", "author": "Author A", "category": "Fiction"},
    {"id": 2, "title": "Book Two", "author": "Author B", "category": "Non-Fiction"},
]

authors = ["Author A", "Author B", "Author C"]
categories = ["Fiction", "Non-Fiction", "Biography"]

# Books Endpoints
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json
    books.append(data)
    return jsonify(data), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.json
    for book in books:
        if book["id"] == book_id:
            book.update(data)
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"})

# Authors Endpoints
@app.route("/authors", methods=["GET"])
def get_authors():
    return jsonify(authors)

@app.route("/authors", methods=["POST"])
def add_author():
    data = request.json
    authors.append(data["name"])
    return jsonify({"name": data["name"]}), 201

# Categories Endpoints
@app.route("/categories", methods=["GET"])
def get_categories():
    return jsonify(categories)

@app.route("/categories", methods=["POST"])
def add_category():
    data = request.json
    categories.append(data["name"])
    return jsonify({"name": data["name"]}), 201

if __name__ == "__main__":
    app.run(debug=True)
