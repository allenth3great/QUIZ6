from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UserRegistrationForm

User = get_user_model()

def register(request):
    User = get_user_model()  # Get the custom user model
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.contact_number = request.POST.get('contact_number')  # Add custom field
            user.save()
            # Optionally send a notification to the admin for approval
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.is_active:  # Check if the user is active
                login(request, user)
                return redirect('home')
            else:
                # Handle inactive user
                return render(request, 'login.html', {'error': 'Account not activated. Please wait for approval.'})
    return render(request, 'login.html')

def create_post(request):
    if hasattr(request.user, 'post'):
        return HttpResponseForbidden("You can only post once.")
    if request.method == 'POST':
        content = request.POST['content']
        post = Post.objects.create(user=request.user, content=content)
        return redirect('home')  # Redirect after posting
    return render(request, 'create_post.html')

def home(request):
    return render(request, 'home.html')

def approve_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect('admin_dashboard')

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'Account not activated. Please wait for approval.'})
    return render(request, 'login.html')
