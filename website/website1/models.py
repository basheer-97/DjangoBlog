from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('Technology', 'Technology'),
        ('News', 'News'),
        ('Sports', 'Sports'),
        ('Food','Food'),
        ('Creative','Creative'),
        ('Education','Education'),
        ('Nature','Nature'),
        ('Personality','Personality')
    )
    cover = models.FileField(default='')
    cover2=models.FileField(default='')
    title =  models.CharField(max_length=2000,default='')
    slug=models.SlugField(default='')
    author=models.CharField(max_length=2000,default='')
    text = models.TextField(default='')
    text_2=models.TextField(default='')
    quote=models.CharField(max_length=2000,default='')
    quote_name=models.CharField(max_length=2000,default='')
    l_heading=models.CharField(max_length=2000,default='')
    l_heading_text=models.CharField(max_length=2000,default='')
    
    category = models.CharField(max_length=2000, choices= CATEGORY_CHOICES)
    created_date = models.DateTimeField(default='')
    

    class Meta:
        ordering=['-created_date']

    def __str__(self):
    		return "%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" %(self.cover,self.cover2,self.title,self.slug,self.author,
            self.text,self.text_2,self.quote,self.quote_name,self.l_heading,self.l_heading_text,self.category,self.created_date)
        #return self.title



    





    