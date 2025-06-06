from django.shortcuts import render, redirect
from django.http import HttpResponse
from ideas.models import shareidea
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def mainpage(request):
    return render(request, "main.html")

def homepage(request):
    if request.user.is_authenticated:
        data = shareidea.objects.all().order_by("-id")
        return render(request, "home.html", {"allData" : data})
    else:
        return redirect("login")

def sharepage(request):
    if request.user.is_authenticated:
        return render(request, "content.html")
    else:
        return redirect("login")

def saveinfo(request):
    if request.method == "POST":
        user_name = request.POST.get("uname")
        full_name = request.POST.get("fname")
        email = request.POST.get("email")
        idea = request.POST.get("idea")
        descpn = request.POST.get("desp")

        data = shareidea(username=user_name, full_name=full_name, email_address=email,idea=idea, descri_ption=descpn)
        
        data.save()

        return redirect("home")

    return HttpResponse("Data successfully saved.....")

def deleteinfo(request, xyz):
    data = shareidea.objects.get(id = xyz)
    data.delete()
    return redirect("home")

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pw")

        usercheck = authenticate(username=username, password=password)

        if usercheck:
            login(request, usercheck)
            return redirect("/home")
        else:
            return redirect("/login")

    return render(request, 'authen/login.html')

def registerpage(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        fullname = request.POST.get("fname")
        email = request.POST.get("email")
        password = request.POST.get("pw")

        User.objects.create_user(username=username, first_name=fullname, email=email, password=password)

    return render(request, 'authen/signup.html')

def logoutpage(request):
    logout(request)
    return redirect("/")