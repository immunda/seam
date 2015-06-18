from seam.core import db
from flask import render_template, Blueprint

bp = Blueprint('main', __name__, template_folder='templates')

def _get_coll(coll_name):
    return db[coll_name]

@bp.route('/computer/')
def computer():
    return render_template('computer.html')

@bp.route('/')
def index():
    all_posts = _get_coll('posts').find().sort('created_at', -1)
    return render_template('index.html', all_posts=all_posts)

@bp.route('/health-check')
def health_check():
    return 'OK'

@bp.route('/post/<slug>/')
def detail(slug):
    post = _get_coll('posts').find_one({'slug' : slug})
    return render_template('detail.html', post=post)
