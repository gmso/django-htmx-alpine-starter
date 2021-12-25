# from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy

from zen_queries import render


# Create your views here.
def root(request):
    request.user.get_all_permissions()
    if request.user.is_authenticated:
        return redirect(reverse_lazy("core:dashboard"))
    return render(request, "index.html")


@login_required
def dashboard(request):
    request.user.get_all_permissions()
    return render(request, "core/dashboard.html")


@login_required
def account(request):
    request.user.get_all_permissions()
    return render(request, "core/account.html")
