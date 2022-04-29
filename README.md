### Study Notes
[Django](https://github.com/getfutureproof/fp_guides_wiki/wiki/Django)

### Demo repo
To run the demo repo code:
1. Fork and clone this repo
2. cd into repo
3. Install requirements
   - `pipenv install -r requirements.txt`
4. Activate your virtual environment
   - `pipenv shell`
4. cd into project and start server
   - `python manage.py runserver` 
5. See the app in action at
   - `http://localhost:8000/`
  
# Exercises
1. Getting Started
   - Create a Django project with one app, 'library'
   - Add views and templates for a home and books show page (`/` and `/books/<id>`)
   - The home page will list all the book titles
   - The show page will list the chosen book title and author
   - Show a custom 404 if book is not found
   - Use dummy data for now:
```python
[
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Liff' 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency' 'author': 'Alexander McCall Smith'}
]
```

2. Add database and models
   - Setup a 'library' database (your choice of db) 
   - Create models for Book and Author
     - Authors have a name
     - Books have a title and a Foreign Key for author
   - Make and run migrations
   - Add your models to your admin dashboard and create some records in the GUI
   - Update your views to take data from the database instead of the dummy data list

3. Add User authentication
   - Create register, login and logout routes
   - Use the UserCreationForm to complete your templates
   - Register some new users via your registration form
   - Make the book show route only available to logged in users
   - Add a new field of 'borrower' to the Book model as a Foreign Key to User
   - In your admin dashboard, assign some books a borrower
   - Update your book show template to show if it is available to loan or not
  
4. Add UI forms
   - Create a new book form accessible at `books/new`
   - On success, the form redirects to the new book's show page
   - Create a button on the book show page
   - If the book is available, on clicking the button, the current User becomes the borrower of that book
   - If the book is on loan by another User, current User sees disabled button
   - If the book is on loan by the current User, on clicking the button, the book is returned
