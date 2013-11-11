from django.db import models
from django.db.models import permalink

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.CharField(max_length=100, default='Jacob Hooey')
    content = models.TextField()
    posted = models.BooleanField(db_index=True, auto_now_add=True)
    
    #This field populates its data from another database table, in this case 
    #Category, so you will need to populate the Category table field first.
    category = models.ForeignKey('post.Category')
    
    def __unicode__(self):
        return u'%s' % self.title
    
    @permalink
    def get_absolute_url(self):
        return ( 'view_blog_post', None, {'slug': self.slug} )
    

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return u'%s' % self.title
    
    @permalink
    def get_absolute_url(self):
        return ( 'view_blog_category', None, {'slug': self.slug} )

"""The __unicode__ function sets the text reference for each record. 
This is used mainly in the automated django admin, but this is still available 
to use on your own site.

The get_absolute_url function defines a URL, again used in the admin area, for 
each record.

Without the @permalink decorator the following would not work. 
This returns a URL calculated from the urls.py file which will be explained 
shortly. I would recommend using this method as it allows you to change the URL 
for a page in only one location.
"""