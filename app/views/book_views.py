from flask import render_template, flash, redirect, request
from app import app
from app.views import main_views
from app.models import books
from app.forms import forms

@app.route('/addBook', methods=['GET', 'POST'])
def addBook():
    '''
    Creates a form for the user to add a new book with its title, author and year of publication.
    If the form is validated, displays entered information to the user before validation.
    '''
    form = forms.BookForm()

    if form.validate_on_submit():
        return render_template("addBook.html", form=form, added=True)

    return render_template("addBook.html",
                           title="Add a new book",
                           form=form)

@app.route('/addBook/validate', methods=['GET', 'POST'])
def validateBook():
    '''
    Validate the entered book and add it to the database
    '''
    print request.form['title']
    if(books.addBook(request.form['title'], request.form['author'], request.form['year'])):
        flash("Book successfully added to the database.")
    else:
        flash("Book already added to the database.")
    return redirect("\index")

@app.route('/initBooks')
def initBooks():
    '''
    Initializes the database with some books
    '''
    if(books.initBooks()):
        flash("Books successfully initialized.")
    else:
        flash("Books already initialized.")
    return redirect("\index")

@app.route('/listAuthors')
def listAuthors():
    '''
    Returns a list of the registered books authors.
    '''
    list = books.getListAuthors()
    return render_template("listAuthors.html", list=list)

@app.route('/listBooks', methods=['GET', 'POST'])
def listBooks():
    '''
    Returns a list of the registered books as strings.
    '''
    title = request.args.get("title") or request.form.get("title")
    author = request.args.get("author") or request.form.get("author")
    year = request.args.get("year") or request.form.get("year")
    list = books.getListBooks(title, author, year)
    return render_template("listBooks.html", list=list)
