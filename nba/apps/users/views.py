from django.views.generic import DetailView, View
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm


class UserCreate(View):
    template_name = 'users/register.html'
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # I can make some operations with user here
            user.save()
            messages.success(self.request, "Your account was created. Now you can log in.")
            return redirect('/')
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        context = {'form': form}

        return render(request, self.template_name, context)


class LoginUser(LoginView):
    template_name = 'users/login.html'
