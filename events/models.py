from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from elementsofrisk.config import COUNTRIES, ELEMENTS

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Create your models here.
class event(models.Model):
    public = models.BooleanField()
    read = models.BooleanField()
    country = models.CharField(max_length=50, choices = COUNTRIES)
    location = models.CharField(max_length=50)
    timedate = models.DateTimeField()
    description = models.CharField(max_length=10000)
    fromId = models.OneToOneField(User,related_name='+')
    toId = models.OneToOneField(User, related_name='+')
    
class message(models.Model):
    messageContent = models.CharField(max_length=10000)
    timedate = models.DateTimeField()
    event = models.ForeignKey(event)
    
class eventForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-eventForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
        
        super(jobSearchForm, self).__init__(*args, **kwargs)
    class Meta:
        model = event
        fields = ('public','country','location','description','toId')
        #widgets = {
        #    'story': Textarea(attrs={'cols': 80, 'rows': 20}),
        #}
        
class messageForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-messageForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit'))
        
        super(jobSearchForm, self).__init__(*args, **kwargs)
    class Meta:
        model = message
        fields = ('messageContent', 'messageContent')