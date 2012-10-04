from django.db import models
from django.forms import ModelForm, Textarea

from elementsofrisk.config import COUNTRIES, ELEMENTS

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-articleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
        
        super(jobSearchForm, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Article
        fields = ('story_date','element','country','story')
        widgets = {
            'story': Textarea(attrs={'cols': 60, 'rows': 20}),
        }
        
class ArticleSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-articleSearchForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
        
        super(jobSearchForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Article
        fields = ('pub_date','story_date','element','country','story','author')
