from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Jacob Hooey')
    slug = models.SlugField(unique=True, max_length=255)
    category = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    #https://docs.djangoproject.com/en/dev/ref/models/instances/#get-absolute-url
    def get_absolute_url(self):
        return reverse( 'blog.views.post', args=[str(self.slug)])
    
    def __unicode__(self):
        return u'%s' % self.title

class Category(models.Model):
    name = models.CharField(max_length=255)


"""Finally, you may notice the inner Meta class on the model. 
This is where you're telling the model class how it should be ordered. 
In this case, you're having the Post objects ordered by the created date. 
The - tells Django to return the objects in a descending order.
(https://docs.djangoproject.com/en/dev/topics/db/models/#meta-options)
"""
class Meta:
    ordering = ['-created']

