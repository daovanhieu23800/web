import abc
from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm

from coffee_app.models import Customer



from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('coffee_app:index'))

def register(request):
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            Customer.objects.create(
            user= new_user,
            name= new_user.username,
            email= new_user.username + "@gmail.com",
            )
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('coffee_app:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
    

