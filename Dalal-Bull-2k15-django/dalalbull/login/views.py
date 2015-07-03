from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from .models import User
@ensure_csrf_cookie
def index(request):
	template=loader.get_template('login/index.html')
	request.session['login']=1
	return HttpResponse(template.render())