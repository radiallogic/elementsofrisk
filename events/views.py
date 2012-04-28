from models import event, eventForm, messageForm
from django.shortcuts import render_to_response

def request(request,id = 0):
    if request.method == 'POST': # If the form has been submitted...
        if id == 0:
            form = eventForm(request.POST) # A form bound to the POST data
        else:
            e = event.objects.get(pk = id)
            form = eventForm(request.POST, instance=e)
            
        if form.is_valid(): # All validation rules pass
            new_event = form.save();
            #return HttpResponseRedirect('/thanks/') # Redirect after POST
            return view(request,id)
    else:
        if id != 0:
            e = event.objects.get(id)
            form = eventForm(instance=e)
        else:
            form = eventForm() # An unbound form

    return render_to_response('events/Request.html', {
        'form': form,
    })

def response(request,id = 0):
    if request.method == 'POST': # If the form has been submitted...
        if id == 0:
            form = messageForm(request.POST) # A form bound to the POST data
        else:
            e = event.objects.get(id)
            form = messageForm(request.POST, instance=e)
            
        if form.is_valid(): # All validation rules pass
            new_event = form.save();
            #
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        if id != 0:
            e = event.objects.get(id)
            form = messageForm(instance=e)
        else:
            form = messageForm() # An unbound form

    return render_to_response('events/Respond.html', {
        'form': form,
    })
    

def view(request,id):
    event = event.objects.get(id = id, user = request.user.id)
    return render_to_response('events/View.html', {
        'event': event,
    })

def viewajax(request):
    pass

def viewlist(request):
    events = event.objects.all().filter(toId = request.user.id)
    return render_to_response('events/ViewList.html', {
        'events': events.__dict__,
    })