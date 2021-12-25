from django.urls import reverse_lazy

import pytest
import allauth.account.views as AllAuthViews
from pytest_django.asserts import assertTemplateUsed

from users.factories import create_user
from users import views as UsersViews


@pytest.mark.parametrize(
    "path,url,view,template",
    [
        (
            "/accounts/signup/",
            "account_signup",
            AllAuthViews.signup,
            "account/signup.html",
        ),
        (
            "/accounts/login/",
            "account_login",
            AllAuthViews.login,
            "account/login.html",
        ),
        (
            "/accounts/inactive/",
            "account_inactive",
            AllAuthViews.account_inactive,
            "account/account_inactive.html",
        ),
        (
            "/accounts/password/reset/",
            "account_reset_password",
            AllAuthViews.password_reset,
            "account/password_reset.html",
        ),
        (
            "/accounts/password/reset/done/",
            "account_reset_password_done",
            AllAuthViews.password_reset_done,
            "account/password_reset_done.html",
        ),
        (
            "/accounts/password/reset/key/12346asd-asd453/",
            "account_reset_password_from_key",
            AllAuthViews.password_reset_from_key,
            "account/password_reset_from_key.html",
        ),
        (
            "/accounts/password/reset/key/done/",
            "account_reset_password_from_key_done",
            AllAuthViews.password_reset_from_key_done,
            "account/password_reset_from_key_done.html",
        ),
    ],
)
@pytest.mark.django_db
def test_views_no_login_required(client, url, view, path, template):
    if url == "account_reset_password_from_key":
        reversed_path = reverse_lazy(
            url,
            kwargs = {
                "uidb36":"12346asd",
                "key":"asd453",
            }
        )
    else:
        reversed_path = reverse_lazy(url)
    assert path == reversed_path

    response = client.get(reversed_path)
    assert response.status_code == 200
    assert response.resolver_match.func == view
    assertTemplateUsed(response, template)


@pytest.mark.parametrize(
    "path,url,view,template,redirected_template",
    [
        (
            "/accounts/logout/",
            "account_logout",
            AllAuthViews.logout,
            "account/logout.html",
            "index.html",
        ),
        (
            "/accounts/password/change/",
            "account_change_password",
            UsersViews.password_change,
            "account/password_change.html",
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

    response = client.get(reversed_path, follow=True)
    assert response.status_code == 200
    assert response.resolver_match.func != view
    assertTemplateUsed(response, redirected_template)

    user = create_user("user", "kjns030")
    client.force_login(user)
    response = client.get(path)
    assert response.status_code == 200
    assert response.resolver_match.func == view
    assertTemplateUsed(response, template)
