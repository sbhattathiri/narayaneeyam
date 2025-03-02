# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# from django.contrib.auth.decorators import login_required
# from django.contrib import messages


# def narayaneeyam_login(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect(
#                 request.GET.get("next", "/")
#             )  # Redirect to a home page or dashboard
#         else:
#             messages.error(request, "Invalid username or password")
#     return render(request, "ayuh_home/login.html")


# @login_required
# def narayaneeyam_logout(request):
#     logout(request)
#     return redirect("login")


# @login_required
def narayaneeyam_home(request):
    return render(request, "ayuh_home/home_template.html", context={})


def narayaneeyam_admin(request):
    return render(request, "ayuh_home/admin_home_template.html", context={})


def narayaneeyam_admission(request):
    return render(
        request,
        "ayuh_home/admissions_home_template.html",
        context={},
    )


def narayaneeyam_inventory(request):
    return render(
        request,
        "ayuh_home/inventory_home_template.html",
        context={},
    )
