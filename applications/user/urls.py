from django.urls import path

from .views import CreateTokenUser


urlpatterns = [
    path(
        "api/user/login",
        CreateTokenUser.as_view(),
        name="login"
    )
]
