import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
  return render(request, "index.html",{'wrapperTimes': range(2), 'debug': settings.DEBUG})

def robots_txt(request):
    path = os.path.join(settings.STATIC_ROOT or settings.STATICFILES_DIRS[0], 'robots.txt')
    with open(path, 'r') as f:
        content = f.read()
    return HttpResponse(content, content_type='text/plain')
def sitemap_xml(request):
    path = os.path.join(settings.STATIC_ROOT or settings.STATICFILES_DIRS[0], 'sitemap.xml')
    with open(path, 'r') as f:
        content = f.read()
    return HttpResponse(content, content_type="application/xml")