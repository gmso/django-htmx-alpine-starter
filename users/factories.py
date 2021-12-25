from users.models import CustomUser


def create_user(username: str, password: str) -> CustomUser:
    user = CustomUser.objects.create_user(username=username, password=password)
    return user
