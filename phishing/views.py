from django.shortcuts import render,redirect
from .models import UserDetails
# Create your views here.
def signin(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    added_user = UserDetails.objects.create(username=username, password=password)
    print(username)
    print(password)
    added_user.save()
    return redirect('findus')
  else:
    return render(request, 'signin.html')
    
def findus(request):
  return render(request, 'findus.html')