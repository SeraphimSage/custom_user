from django.shortcuts import render, HttpResponseRedirect, reverse
from custom_user_app.models import MyUser
from custom_user_app.forms import SignupForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from custom_user.settings import AUTH_USER_MODEL

# Create your views here.


def index_view(request):
    custom_users = MyUser.objects.all()
    return render(request, "index.html", {"AUTH_USER_MODEL": AUTH_USER_MODEL})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                username=data.get("username"),
                                password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                username=data.get("username"),
                password=data.get("password"),
                age=data.get("age"),
                display_name=data.get("display_name"))
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
