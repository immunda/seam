from django.shortcuts import render_to_response
from django.template.response import TemplateResponse
from pymongo import Connection
from djpjax import pjax

# Get database and any collections
db = Connection().seam

def _get_coll(coll_name):
    return db[coll_name]

def computer(request):
    return TemplateResponse(request, 'computer.html', {})

@pjax()
def index(request):
    all_posts = _get_coll('posts').find().sort('created_at', -1)
    return TemplateResponse(request, 'index.html', {'all_posts' : all_posts})

@pjax()
def detail(request, slug):
    post = _get_coll('posts').find_one({'slug' : slug})
    return TemplateResponse(request, 'detail.html', {'post' : post})