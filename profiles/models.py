from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from elementsofrisk.config import COUNTRIES, ELEMENTS, SKILL, LOOKINGFOR, SPORT

class activities(models.Model):
    element = models.CharField(max_length = 1, choices = ELEMENTS)
    name = models.CharField(max_length = 50)
    
class skillLevel(models.Model):
    skill = models.CharField(max_length=500, null = True)
    order = models.IntegerField()
    
class userActivities():
    user = models.OneToOneField(User)
    skill = models.ForeignKey(skillLevel)
    activity = models.ForeignKey(activities)

class memberAditional(models.Model):
    # basics
    nickname = models.CharField(max_length=100, null = True)
    user = models.OneToOneField(User)
    
    # details
    dob = models.DateField('dob', null = True)
    homeCountry = models.CharField(max_length=50, choices = COUNTRIES, null = True)
    homeCity = models.CharField(max_length=200, null = True)
    currentLocation = models.CharField(max_length=200, null = True)
    
    # profile
    favouriteElement = models.CharField(max_length = 1, choices = ELEMENTS, null = True)
    aboutme = models.CharField(max_length=20000, null = True)
    lookingfor = models.CharField(max_length=50, choices = LOOKINGFOR, null = True)
    
    def __unicode__(self):
        return self.nickname

class memberAditionalForm(ModelForm):
    class Meta():
        model = memberAditional
        fields = ('nickname','dob','homeCountry','homeCity','favouriteElement','aboutme','lookingfor')
        
class memberAditionalSearchForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(memberAditionalSearchForm, self).__init__(*args, **kwargs)
        self.fields['homeCountry'].label = "Home Country"
        self.fields['homeCity'].label = "Home City"
        self.fields['favouriteElement'].label = "Element"
        self.fields['aboutme'].label = "About Me"
        self.fields['lookingfor'].label = "Looking For"
    class Meta():
        model = memberAditional
        fields = ('nickname','dob','homeCountry','homeCity','favouriteElement','aboutme','lookingfor')

        
class registerForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField( widget=forms.PasswordInput, label="Your Password" )
    confirmPassword = forms.CharField( widget=forms.PasswordInput, label="Confirm Your Password" )
    email = forms.EmailField(label = 'Email' )
    confirmEmail = forms.EmailField(label = 'Confirm Email')
    