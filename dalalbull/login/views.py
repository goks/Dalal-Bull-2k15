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
@ensure_csrf_cookie
def login(request):
	if(request.session['login']==1):
		u = User(user_id=request.POST['username'], first_name=request.POST['firstname'], last_name=request.POST['lastname'], email=request.POST['email'],)
		u.save()
		request.session['login']=0
		request.session['dashboard']=1
		return HttpResponse('success');
	return HttpResponse("Access Denied")
def dashboard(request):
	if(request.session['dashboard']==1):
		request.session['dashboard']=0
		return HttpResponse("DashBoard")
	return HttpResponse("Access Denied")
