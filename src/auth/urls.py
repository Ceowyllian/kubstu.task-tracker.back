from django.urls import include, path, re_path

from .views import TokenCreateView, TokenDestroyView

urlpatterns = [
    path("", include("djoser.urls")),
    re_path(r"^token/login/?$", TokenCreateView.as_view(), name="login"),
    re_path(r"^token/logout/?$", TokenDestroyView.as_view(), name="logout"),
]
