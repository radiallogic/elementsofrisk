# Create your views here.
#from random import 
from random import *
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from stories.models import Article, ArticleForm, ArticleSearchForm
from django.shortcuts import render_to_response

    
def add(request,id=0):

    if request.method == 'POST': 
        if id == 0:
            form = ArticleForm(request.POST) # A form bound to the POST data
        else:
            article = Article.objects.get(id)
            form = ArticleForm(request.POST, instance=article)
            
        if form.is_valid(): # All validation rules pass
            new_article = form.save();
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        if id != 0:
            article = Article.objects.get(id)
            form = ArticleForm(instance=article)
        else:
            form = ArticleForm() # An unbound form

    return render_to_response('stories/ArticleForm.html', {
        'form': form,
    }, context_instance=RequestContext(request))

def search(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ArticleSearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            q = Entry.objects.all() #headline__startswith="What"
            filters = {country: 'country__contains', pub_date: '__contains', story_date: '__contains', element: '__contains', author: '__icontains', story: '__icontains'}
            for key,var in filters:
                q = q.filter(var = form.cleaned_data[key])
        return render_to_response('stories/List.html', {
            'storylist': q,
        }, context_instance=RequestContext(request))
    else:
        form = ArticleSearchForm() # An unbound form

    return render_to_response('stories/Search.html', {
        'form': form,
    }, context_instance=RequestContext(request))
    
    
def rand(request):
    s = Article.objects.get(id_max)
    num = randrange(1,s.id)
    show(request,num)
    
def show(request, story_id):
    try:
        s = Article.objects.get(pk=story_id)
    except Article.DoesNotExist:
        raise Http404
    return render_to_response('stories/Show.html', context_instance=RequestContext(request))

def list(request, type = '-pub_date'):  
    story_list = Article.objects.all().order_by(type)[:5]
    return render_to_response('stories/List.html', {
        'storylist': story_list,
    }, context_instance=RequestContext(request))
    
def listpubdate(request):
    return list(request,'-pub_date')
    
def liststorydate(request):
    return list(request,"-story_date")
    
def listauth(request):
    return list(request,"-author")