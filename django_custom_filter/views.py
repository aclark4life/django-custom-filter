from django.shortcuts import render_to_response
import datetime


def root(request):
    now = datetime.datetime.now()
    return render_to_response('root.html', {'now': 'it is NOW %s' % now})
