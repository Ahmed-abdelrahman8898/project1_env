from flask import render_template, request, Blueprint
from flaskblog.models import Post


main=Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
def hello_world():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=3)
    return render_template('Home.html',posts=posts)

@main.route('/about')
def hello_world2():
    return render_template('About.html',title='sexsexsex')