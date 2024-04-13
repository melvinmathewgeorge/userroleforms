from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from users.forms import RegisterUserForm, LoginUserForm
from users.models import User
from django.http import Http404

def register_user_view(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            messages.success(request, f'User created for {name} successfully')
            return redirect('users:login_user')
        else:
            return render(request, 'users/register_user.html', {'form':form})
    else:
        form = RegisterUserForm()
        context = {
            'form':form
        }
    return render(request, 'users/register_user.html', context)

def login_user_view(request):
    if request.user.is_authenticated:
        return redirect('users:user_redirect')
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.name}!')
                if user.role == user.STUDENT:
                    return redirect('users:student_page')
                elif user.role == user.STAFF:
                    return redirect('users:staff_page')
                elif user.role == user.ADMIN:
                    return redirect('users:admin_page')
                elif user.role == user.EDITOR:
                    return redirect('users:editor_page')  
            else:
                messages.warning(request, 'Invalid email or password.')
    else:
        form = LoginUserForm()

    return render(request, 'users/login_user.html', {'form': form})

def user_redirect_view(request):
    user = request.user
    if user.role == User.STUDENT:
        return redirect('users:student_page')
    elif user.role == User.STAFF:
        return redirect('users:staff_page')
    elif user.role == User.ADMIN:
        return redirect('users:admin_page')
    elif user.role == User.EDITOR:
        return redirect('users:editor_page')

def logout_user_view(request):
    logout(request)
    return redirect('users:login_user')

def student_page_view(request):
    if request.user.is_authenticated and request.user.role == User.STUDENT:
        return render(request,'users/student.html')
    raise Http404

def staff_page_view(request):
    if request.user.is_authenticated and request.user.role == User.STAFF:
        return render(request,'users/staff.html')
    raise Http404

def admin_page_view(request):
    if request.user.is_authenticated and request.user.role == User.ADMIN:
        return render(request,'users/admin.html')
    raise Http404

def editor_page_view(request):
    if request.user.is_authenticated and request.user.role == User.EDITOR:
        return render(request,'users/editor.html')
    raise Http404



        