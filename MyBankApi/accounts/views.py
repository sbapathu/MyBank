# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from accounts.forms import UserRegistrationForm, UserLoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class UserRegistrationView(APIView):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'user_registration.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_registration_success')
        return render(request, 'user_registration.html', {'form': form})

class UserLoginView(APIView):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'user_login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_login_success')
            else:
                form.add_error(None, 'Invalid username or password.')
        return render(request, 'user_login.html', {'form': form})

class UserLogoutView(APIView):
    def get(self, request):
        logout(request)
        return redirect('user_logout_success')
    
class UserRegistrationSuccessView(APIView):
    def get(self, request):
        return render(request, 'user_registration_success.html')
    
class UserLoginSuccessView(APIView):
    def get(self, request):
        return render(request, 'user_login_success.html')
    
