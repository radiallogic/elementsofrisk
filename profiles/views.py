from django.http import HttpResponse
from django.template import loader, RequestContext, Context
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import redirect_to_login, password_change_done, password_change, logout, login
from django.shortcuts import render_to_response

from profiles.models import memberAditional, memberAditionalForm, registerForm, memberAditionalSearchForm

from django.views.decorators.csrf import csrf_protect, csrf_exempt


@login_required
def viewProfile(request):
    print request.user.id
    userinfo = memberAditional.objects.get(user = request.user.id)
    return render_to_response('profiles/View.html', {
        'userinfo': userinfo.__dict__,
    })
    
@login_required
def editProfile(request):
    form = None
    if request.method == 'POST': # If the form has been submitted...
        form = memberAditionalForm(request.POST, instance = memberAditional.objects.get(user = request.user.id)) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            form.save()
            return viewProfile(request)
            
    if form == None:
        form = memberAditionalForm( instance = memberAditional.objects.get(user = request.user.id) )
    return render_to_response('profiles/Edit.html', {
            'form': form,
        }, context_instance=RequestContext(request))

@login_required
def addFriend(request):
    pass

@login_required
def leaveReview(request):
    ''' if positive then add as friend '''
    pass

@login_required
def searchProfiles(request):
    if request.method == 'POST': # If the form has been submitted...
        form = memberAditionalSearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            q = Entry.objects.all() #headline__startswith="What"
            filters = {homeCountry: '__contains', homeCity: '__contains', story_date: '__contains', element: '__contains', author: '__contains', story: '__contains'}
            for key,var in filters:
                q = q.filter(var = form.cleaned_data[key])
            return render_to_response('profiles/List.html', {
                'profiles': q,
            }, context_instance=RequestContext(request))
        else:
            print form.errors
    else:
        form = memberAditionalSearchForm() # An unbound form

    return render_to_response('profiles/Search.html', {
        'form': form,
    }, context_instance=RequestContext(request))



def register(request):
    form = None
    if request.method == 'POST': # If the form has been submitted...
        
        form = registerForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            c_p = form.cleaned_data['confirmPassword']
            e = form.cleaned_data['email']
            c_e = form.cleaned_data['confirmEmail']
            
            if p == c_p and e == c_e:
                userObj = User.objects.create_user(u, e, p)
                userObj.save()
                userdata = memberAditional(user = userObj) 
                userdata.save()
                print "saved"
                user = authenticate(username=u, password=p)
                if user is not None:
                    if user.is_active:
                        login(request, user)

                return render_to_response('profiles/WhatNext.html', {
                    'username': u,
                }, context_instance=RequestContext(request))
        else:
            print "notvalid"
    if form == None:
        form = registerForm() # An unbound form
    return render_to_response('profiles/Register.html', {
            'form': form,
        }, context_instance=RequestContext(request))
    
    
def whatNext(request):
    return render_to_response('profiles/WhatNext.html', {
            'username': request.user.username,
        }, context_instance=RequestContext(request))