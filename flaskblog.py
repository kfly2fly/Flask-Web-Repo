from flask import Flask, redirect, url_for, render_template, request, flash, session
# from forms import RegistrationForm, LoginForm
from datetime import timedelta


app = Flask(__name__)

posts = [
    {
        'author': 'Keenan Flynn',
        'title': "I'm back",
        'content': 'Finally getting around to working on the site some more. Refreshing myself on my past code before I dive into some new stuff',
        'date_posted': 'October 15, 2021'
    },
    {
        'author': 'Keenan Flynn',
        'title': 'Database Day',
        'content': 'Learning about databases today with SQLAlchemy, finally got some routing issues figured out',
        'date_posted': 'December 29, 2020'
    },
    {
        'author': 'Keenan Flynn',
        'title': 'Blog Post 5',
        'content': 'Working on this webapp the day after my birthday, feeling kind of rough, my friends thought it would be a good idea to get me several tequila shots',
        'date_posted': 'December 29, 2020'
    },
    {
        'author': 'Keenan Flynn',
        'title': 'Birthday Blog',
        'content': 'Today is my birthday and Christmas was 3 days ago. I got a hammock and some frisbee golf frisbees!!',
        'date_posted': 'December 28, 2020'
    },
    {
        'author': 'Keenan Flynn',
        'title': 'Blog Post 3',
        'content': 'Today I went to the doctor and was positive for strep:/',
        'date_posted': 'December 18, 2020'
    },
    {
        'author': 'Keenan Flynn',
        'title': 'Blog Post 2',
        'content': 'My new nephew Mack was born today!!',
        'date_posted': 'December 16, 2020'
    },
    {
        'author': 'Keenan Flynn',
        'title': 'First Blog Post',
        'content': 'I got a 4.09 this semester',
        'date_posted': 'December 16, 2020'
    }
]

# Beginning of Routes
@app.route("/")
@app.route("/home/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/blog")
def blog():
    return render_template('blog.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
