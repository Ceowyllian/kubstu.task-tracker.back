from datetime import timedelta

from djoser.views import TokenCreateView as DjoserTokenCreateView
from djoser.views import TokenDestroyView as DjoserTokenDestroyView
from djoser.views import UserViewSet as DjoserUserViewSet

__all__ = [
    "TokenCreateView",
    "TokenDestroyView",
]


class TokenCreateView(DjoserTokenCreateView):

    def _action(self, serializer):
        response = super()._action(serializer)
        response.set_cookie(
            key="auth_token",
            value=response.data["auth_token"],
            max_age=timedelta(days=15),
            secure=True,
            httponly=True,
            samesite="Strict",
        )
        return response


class TokenDestroyView(DjoserTokenDestroyView):
    def post(self, request):
        response = super().post(request)
        response.delete_cookie("auth_token")
        return response


class UserViewSet(DjoserUserViewSet):
    pass
