from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import TokenCreateView, TokenDestroyView, UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path(r"^token/login/?$", TokenCreateView.as_view(), name="login"),
    re_path(r"^token/logout/?$", TokenDestroyView.as_view(), name="logout"),
]
