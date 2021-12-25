import pytest

from users.models import CustomUser
from users.factories import create_user


@pytest.mark.django_db
def test_create_user():
    assert CustomUser.objects.count() == 0

    user_a = create_user("johnny", "pa55word_")
    assert CustomUser.objects.count() == 1
    assert CustomUser.objects.all()[0] == user_a

    user_b = create_user("pipboy", "p9o8haakjn")
    assert CustomUser.objects.count() == 2
    assert set(CustomUser.objects.all()) == {user_a, user_b}
