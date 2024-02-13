from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

# Beginning of Routes
@main.route("/")
@main.route("/home/")
def home():
    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html')


@main.route("/blog")
def blog():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('blog.html', posts=posts)




@main.route("/home2")
def home2():
    return render_template('home2.html')
