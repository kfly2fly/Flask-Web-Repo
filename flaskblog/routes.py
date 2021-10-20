from flask import redirect, url_for, render_template, request, flash, session, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccount
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image

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


@app.route("/register", methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data.upper(), password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.upper()).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pic', picture_fn)
    form_picture.save(picture_path)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

@app.route("/account", methods = ['GET', 'POST'])
@login_required
def account():
    form = UpdateAccount()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = form.username.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updatad!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pic/'+ current_user.image_file)
    return render_template('account.html', title = 'Account', image_file=image_file, form=form)
