from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView

import core.views as views


app_name = "core"
urlpatterns = [
    path("", views.root, name="root"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("account/", views.account, name="account"),
]
