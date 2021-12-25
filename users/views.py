from django.urls import reverse_lazy

from allauth.account.views import login_required, PasswordChangeView

# Create your views here.
class PasswordChangeViewOverridden(PasswordChangeView):
    """Override original Allauth's view to customize success url"""
    success_url = reverse_lazy("core:account")

password_change = login_required(PasswordChangeViewOverridden.as_view())
