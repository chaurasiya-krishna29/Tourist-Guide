from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm, ContactForm
from .models import Contact

from django.utils import timezone
from .models import CustomUser


from django.contrib.auth.decorators import login_required

# Add login_required decorator to index view
@login_required(login_url='login')
def index(request):
    return render(request, 'home/index.html')
@login_required(login_url='login')

def about(request):
    return render(request, 'home/about.html')
@login_required(login_url='login')

def explore(request):
    return render(request, 'home/explore.html')


@login_required(login_url='login')

def contact(request):
    if request.method == 'POST':
        try:
            contact = Contact.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                message=request.POST.get('message')
            )
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again.')
            return redirect('contact')
    
    return render(request, 'home/contact.html')


def signup_page(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        try:
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            city = request.POST.get('city')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                messages.error(request, 'Passwords do not match!')
                return redirect('signup')

            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists!')
                return redirect('signup')

            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                mobile=mobile,
                city=city
            )
            
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')

        except Exception as e:
            messages.error(request, str(e))
            return redirect('signup')

    return render(request, 'home/SignUp.html')

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Change this part
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('index')
            else:
                messages.error(request, 'Invalid email or password!')
        except Exception as e:
            messages.error(request, str(e))
        
    return render(request, 'home/login.html')

@login_required(login_url='login')
def logout_page(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

@login_required(login_url='login')
def profile_page(request):
    return render(request, 'home/profile.html')

