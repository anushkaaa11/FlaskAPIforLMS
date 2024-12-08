# Library Management System - Flask API

This is a **Flask-based API** for a Library Management System, designed to manage books and members with **CRUD (Create, Read, Update, Delete) operations** and the **search functionality** for books by title or author. The application uses **SQLite** as the database for storing data.

---

## Table of Contents:
1. [Project Overview](#project-overview)
2. [How to Run the Project](#how-to-run-the-project)
3. [How to Use Postman](#how-to-use-postman)
4. [Design Choices](#design-choices)
5. [Assumptions & Limitations](#assumptions-limitations)

---

### Project Overview

This project is a Flask-based API that allows you to:
- Manage **Books** and **Members** in a library.
- Perform CRUD operations (Create, Read, Update, Delete) on books and members.
- Search books by **title** or **author**.

It includes two main entities:
- **Books**: Represents a book in the library, with attributes like title, author, year, and genre.
- **Members**: Represents the library members, with attributes like name, email, and registration date.

---

### How to Run the Project

Follow these steps to get the project running on your local machine:

1. **Clone the repository** (if you haven’t already):

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Python**:
   Ensure that Python 3.x is installed on your system. You can verify by running:

   ```bash
   python --version
   ```

3. **Install Flask**:

   Since we are using **Flask** for building the API, make sure Flask is installed. Run the following command in your terminal:

   ```bash
   pip install flask
   ```

4. **Run the application**:

   In the project directory, run the following command to start the Flask application:

   ```bash
   python app.py
   ```

   This will start the development server, and you can access the application at:

   ```
   http://127.0.0.1:5000
   ```

5. **Test the API**:
   - You can use **Postman** or any API testing tool to test the endpoints:
     - `GET /books` - List all books.
     - `POST /books` - Add a new book.
     - `PUT /books/<id>` - Update book information by ID.
     - `DELETE /books/<id>` - Delete a book by ID.
     - `GET /search` - Search for books by title or author.
   
---

### How to Use Postman

Follow the steps below to interact with the Flask API using **Postman**:

1. **Open Postman**:
   - If you don’t have Postman installed, you can download it from [Postman Download](https://www.postman.com/downloads/).
   - Open Postman after installation.

2. **Testing the GET /books endpoint**:
   - In Postman, create a new **GET** request.
   - Enter the following URL in the request bar:
     ```
     http://127.0.0.1:5000/books
     ```
   - Click **Send**.
   - You should get a response with a list of all books in JSON format.

3. **Testing the POST /books endpoint** (Adding a new book):
   - In Postman, create a new **POST** request.
   - Enter the following URL:
     ```
     http://127.0.0.1:5000/books
     ```
   - Select **Body** in Postman, and choose **raw** as the type. Set the body to **JSON** format.
   - Example JSON to add a new book:
     ```json
     {
       "title": "The Great Gatsby",
       "author": "F. Scott Fitzgerald",
       "year": 1925,
       "genre": "Fiction"
     }
     ```
   - Click **Send**.
   - You should receive a response confirming that the book has been added.

4. **Testing the PUT /books/{id} endpoint** (Updating a book):
   - In Postman, create a new **PUT** request.
   - Enter the URL (replace `{id}` with an actual book ID):
     ```
     http://127.0.0.1:5000/books/1
     ```
   - Select **Body** in Postman, and choose **raw** as the type. Set the body to **JSON** format.
   - Example JSON to update the book:
     ```json
     {
       "title": "The Great Gatsby (Updated)",
       "author": "F. Scott Fitzgerald",
       "year": 1925,
       "genre": "Classic Fiction"
     }
     ```
   - Click **Send**.
   - You should receive a response confirming that the book has been updated.

5. **Testing the DELETE /books/{id} endpoint** (Deleting a book):
   - In Postman, create a new **DELETE** request.
   - Enter the URL (replace `{id}` with an actual book ID):
     ```
     http://127.0.0.1:5000/books/1
     ```
   - Click **Send**.
   - You should receive a response confirming that the book has been deleted.

6. **Testing the GET /search endpoint** (Searching for books by title or author):
   - In Postman, create a new **GET** request.
   - Enter the following URL (replace `{search_term}` with a title or author name):
     ```
     http://127.0.0.1:5000/search?query={search_term}
     ```
   - Click **Send**.
   - You should get a response with books matching the search query (either title or author).

---

### Design Choices

1. **Flask**: 
   - Flask was chosen for building this API due to its simplicity and ease of use for small projects like this one. It provides the necessary features to quickly set up routes and handle HTTP requests.

2. **SQLite Database**: 
   - SQLite was chosen for the database because it is a lightweight, serverless database that is easy to set up and manage. It stores data locally in a `.db` file, which is perfect for this small project. No need for a heavy database server like MySQL or PostgreSQL.

3. **Data Model**:
   - **Books** and **Members** are the two core entities. The **Books** table stores the book information (title, author, year, genre), while the **Members** table stores the member details (name, email, registration date).
   - The system uses **SQL queries** for interacting with the database, including CRUD operations for both entities.

4. **Search Functionality**:
   - The search functionality is simple: it queries the database for books by title or author using the `LIKE` operator in SQL. This makes searching for books efficient within the small-scale database.

---

### Assumptions & Limitations

1. **Assumptions**:
   - The application assumes that the user has **Python** installed and is familiar with running Python applications.
   - The **SQLite database** will be created automatically the first time the application runs. There is no need for complex setup or migration scripts.
   - Data input is assumed to be **valid** (i.e., no complex validation is done on inputs).

2. **Limitations**:
   - **No Authentication**: The application does not require authentication or authorization, so anyone with access to the API can perform any action (e.g., add, update, delete books).
   - **Basic Search**: The search functionality only supports searching by title or author using basic string matching. Advanced searching features, like partial matches or filtering by genre, are not implemented.
   - **Data Validation**: There is minimal validation of input data. For instance, when adding books or members, the input data is assumed to be in the correct format. More comprehensive validation could be added (e.g., ensuring all required fields are present, valid email format).
   - **Production Readiness**: The application is designed for development use and is not production-ready. For production deployment, a more robust WSGI server (such as **Gunicorn**) would be needed, along with error handling, logging, and other enhancements.

---

### Conclusion

This Flask-based Library Management System API provides essential CRUD functionality for books and members and includes basic search capabilities. It is lightweight, simple to use, and ideal for learning purposes. You can easily extend it with more advanced features, such as user authentication, more complex search functionalities, and better error handling.

---
