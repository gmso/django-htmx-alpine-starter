from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from allauth.account import views as AllauthViews

import debug_toolbar

from users import views as UsersViews

urlpatterns = [
    # Django admin:
    path("ZCFtd8UunfnyLURaY3fd/", admin.site.urls),
    # Local apps:
    path("", include("core.urls", namespace="core")),
]

# Allauth
urlpatterns += [
    path("accounts/signup/", AllauthViews.signup, name="account_signup"),
    path("accounts/login/", AllauthViews.login, name="account_login"),
    path("accounts/logout/", AllauthViews.logout, name="account_logout"),
    path(
        "accounts/password/change/",
        UsersViews.password_change,
        name="account_change_password",
    ),
    # path("accounts/password/set/", AllauthViews.password_set, name="account_set_password"),
    path(
        "accounts/inactive/",
        AllauthViews.account_inactive,
        name="account_inactive",
    ),
    # # E-mail
    # path("email/", AllauthViews.email, name="account_email"),
    # path(
    #     "confirm-email/",
    #     AllauthViews.email_verification_sent,
    #     name="account_email_verification_sent",
    # ),
    # re_path(
    #     r"^confirm-email/(?P<key>[-:\w]+)/$",
    #     AllauthViews.confirm_email,
    #     name="account_confirm_email",
    # ),
    # # password reset
    path(
        "accounts/password/reset/",
        AllauthViews.password_reset,
        name="account_reset_password",
    ),
    path(
        "accounts/password/reset/done/",
        AllauthViews.password_reset_done,
        name="account_reset_password_done",
    ),
    re_path(
        r"^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        AllauthViews.password_reset_from_key,
        name="account_reset_password_from_key",
    ),
    path(
        "accounts/password/reset/key/done/",
        AllauthViews.password_reset_from_key_done,
        name="account_reset_password_from_key_done",
    ),
]


if settings.DEV_MODE:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
