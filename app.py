from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to initialize the SQLite database
def init_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Create books table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER
        )
    ''')

    # Create members table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Call init_db() to create tables when the app starts
init_db()

# GET /books - Retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books')
    books = cursor.fetchall()
    conn.close()
    
    books_list = [{"id": book[0], "title": book[1], "author": book[2], "year": book[3]} for book in books]
    return jsonify(books_list)

# POST /books - Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data['title']
    author = data['author']
    year = data['year']
    
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO books (title, author, year) VALUES (?, ?, ?)', (title, author, year))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Book added successfully"}), 201

# PUT /books/<id> - Update book details by ID
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    year = data.get('year')
    
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    if title:
        cursor.execute('UPDATE books SET title = ? WHERE id = ?', (title, id))
    if author:
        cursor.execute('UPDATE books SET author = ? WHERE id = ?', (author, id))
    if year:
        cursor.execute('UPDATE books SET year = ? WHERE id = ?', (year, id))
    
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Book updated successfully"})

# DELETE /books/<id> - Delete a book by ID
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Book deleted successfully"})

# GET /search - Search books by title or author
@app.route('/search', methods=['GET'])
def search_books():
    query = request.args.get('query', '')  # Get search query from URL parameters
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM books
        WHERE title LIKE ? OR author LIKE ?
    ''', ('%' + query + '%', '%' + query + '%'))
    books = cursor.fetchall()
    conn.close()
    
    books_list = [{"id": book[0], "title": book[1], "author": book[2], "year": book[3]} for book in books]
    return jsonify(books_list)

# GET /members - Retrieve all members
@app.route('/members', methods=['GET'])
def get_members():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM members')
    members = cursor.fetchall()
    conn.close()
    
    members_list = [{"id": member[0], "name": member[1], "email": member[2]} for member in members]
    return jsonify(members_list)

# POST /members - Add a new member
@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    name = data['name']
    email = data['email']
    
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO members (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Member added successfully"}), 201

# DELETE /members/<id> - Delete a member by ID
@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM members WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Member deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
