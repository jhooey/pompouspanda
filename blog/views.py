from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post, Category

#The following is for your index page, which will display a list of all your 
#categories, and 5 most recent posts.
def index(request):
    return render_to_response('blog/index.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })
    
"""In the other two functions view_post & view_category we use one of the 
rather useful Django shortcuts. This queries the database trying to match where 
slug=slug, the first slug being the field in the model, the second slug being 
the input into the function call"""
def view_post(request, slug):   
    return render_to_response('blog/view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })
def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })