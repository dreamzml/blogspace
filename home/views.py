# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import datetime



def index(request):

    now = datetime.datetime.now()
    template_var = dict()
    template_var['now'] = now
    # html = "<html><body>It is now %s.</body></html>" % now

    # return HttpResponse(html)
    return render_to_response("index.html", template_var, context_instance=RequestContext(request))

