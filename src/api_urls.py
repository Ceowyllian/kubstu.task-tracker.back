from django.urls import include, path

urlpatterns = [
    path(r"auth/", include("auth.urls")),
]
