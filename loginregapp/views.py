from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
  return redirect('/register/')

def register(request):
  if request.method == 'POST':
    # sign up
    errors = User.objects.validate_user(request.POST['username'], request.POST['password'])
    if errors:
      for key in errors:
        messages.error(request, errors[key])
        return redirect('/login/')

    password = request.POST['password']
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(username=request.POST['username'], password=hashed_password)
    request.session['user_id'] = user.id
    return redirect('/home/')
  return render(request, 'registration.html')

def login(request):
  if request.method == 'POST':
    # check login info
    try:
      user = User.objects.get(username=request.POST['username'])
      if user:
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
          request.session['user_id'] = user.id
          return redirect('/home/')
    except:
      messages.error(request, f"The username {request.POST['username']} does not exist")
      return redirect('/login/')
    return redirect('/login/')
  return render(request, 'login.html')

def home(request):
  return render(request, 'home.html')
