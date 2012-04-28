# Create your views here.
from elementsofrisk.events.models import event, message
from elementsofrisk.profiles.models import memberAditionalSearchForm
from django.http import HttpResponseRedirect

from django.shortcuts import render_to_response

def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('portal')
    return render_to_response('index.html', { })

def portal(request):
    messages = {}
    events = event.objects.all().filter(toId = request.user.id)
    for e in events:
        messages = message.objects.all().filter(event = e)
        
    return render_to_response('index/portal.html', {
        'events': events.__dict__,
        'form': memberAditionalSearchForm,
    })