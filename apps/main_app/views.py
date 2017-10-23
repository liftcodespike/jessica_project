from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Comment

def index(request):
	if 'user_first_name' not in request.session:
		return redirect('/')
	context = {
		'other_users': User.objects.exclude(id = request.session['user_id'])	
	}
	return render(request, 'main_app/index.html', context)


def show(request, id):
	if 'user_first_name' not in request.session:
		return redirect('/')
	context = {
		'shown_user': User.objects.get(id= id)
	}
	return render(request, 'main_app/show.html', context)

def addComment(request):
	if 'user_first_name' not in request.session:
		return redirect('/')
	Comment.objects.create(content = request.POST['content'], user = User.objects.get(id = request.POST['user_id']), poster= User.objects.get(id = request.POST['poster_id']))
	return redirect('/show/' + request.POST['user_id'])
