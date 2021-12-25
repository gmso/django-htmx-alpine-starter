from django.urls import reverse_lazy

import pytest
from pytest_django.asserts import assertTemplateUsed

import core.views as views
from users.factories import create_user


@pytest.mark.parametrize(
    "path,url,view,template",
    [
        ("/", "core:root", views.root, "index.html"),
    ],
)
def test_views_no_login_required(client, url, view, path, template):
    reversed_path = reverse_lazy(url)
    assert path == reversed_path

    response = client.get(path)
    assert response.status_code == 200
    assert response.resolver_match.func == view
    assertTemplateUsed(response, template)


@pytest.mark.parametrize(
    "path,url,view,template,redirected_template",
    [
        (
            "/dashboard/",
            "core:dashboard",
            views.dashboard,
            "core/dashboard.html",
            "account/login.html",
        ),
        (
            "/account/",
            "core:account",
            views.account,
            "core/account.html",
            "account/login.html",
        ),
    ],
)
@pytest.mark.django_db
def test_views_login_required(
    client, url, view, path, template, redirected_template
):
    reversed_path = reverse_lazy(url)
    assert path == reversed_path

    response = client.get(path, follow=True)
    assert response.status_code == 200
    assert response.resolver_match.func != view
    assertTemplateUsed(response, redirected_template)

    user = create_user("user", "kjns030")
    client.force_login(user)
    response = client.get(path)
    assert response.status_code == 200
    assert response.resolver_match.func == view
    assertTemplateUsed(response, template)


@pytest.mark.django_db
def test_root_view_redirects_to_dashboard_if_user_is_authenticated(client):
    url_name = "core:root"

    response = client.get(reverse_lazy(url_name), follow=True)
    assert response.status_code == 200
    assert response.resolver_match.func == views.root
    assertTemplateUsed(response, "index.html")

    user = create_user("user", "pjns23awd")
    client.force_login(user)

    response = client.get(reverse_lazy(url_name), follow=True)
    assert response.status_code == 200
    assert response.resolver_match.func == views.dashboard
    assertTemplateUsed(response, "core/dashboard.html")
