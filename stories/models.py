from django.db import models
from django.forms import ModelForm, Textarea

from elementsofrisk.config import COUNTRIES, ELEMENTS

class Article(models.Model):
    country = models.CharField(max_length=50, choices = ELEMENTS)
    pub_date = models.DateTimeField('date published')
    story_date = models.DateTimeField('date of story')
    element = models.CharField(max_length = 1, choices = ELEMENTS)
    author = models.CharField(max_length=200)
    story = models.CharField(max_length=20000)
    
    def __unicode__(self):
        return self.title
    
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('story_date','element','country','story')
        widgets = {
            'story': Textarea(attrs={'cols': 60, 'rows': 20}),
        }
        
class ArticleSearchForm(ModelForm):
    class Meta:
        model = Article
        fields = ('pub_date','story_date','element','country','story','author')
