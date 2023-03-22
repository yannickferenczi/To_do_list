from django.http import HttpResponse
from django.shortcuts import render

from accounts.forms import MyCustomUserCreationForm


def signup(request):
    signup_errors = {}
    if request.method == 'POST':
        form = MyCustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Merci de vous être inscrit.")
        else:
            signup_errors["errors"] = form.errors
    form = MyCustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form, 'errors': signup_errors})
