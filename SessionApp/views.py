from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout,  get_user_model


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
            "form":form }
    if request.user.is_authenticated:
        return redirect('/home')
    if form.is_valid():
        username = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home/")
        else:
            print("Error")
    return render(request,"auth/login.html",context)


def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')


User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        new_user = User.objects.create_user(
        nombre = form.cleaned_data["nombre"],
        email = form.cleaned_data["email"],
        password = form.cleaned_data["contrasena"],
        domicilio = form.cleaned_data["domicilio"],
        telefono = form.cleaned_data["telefono"],
        )
        return redirect('/home')
    return render(request, "auth/register.html", context)


