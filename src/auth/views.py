from datetime import timedelta

from djoser.views import TokenCreateView as DjoserTokenCreateView
from djoser.views import TokenDestroyView as DjoserTokenDestroyView
from djoser.views import UserViewSet as DjoserUserViewSet

from shared.api import SCHEMA_TAG_AUTH, extend_schema

__all__ = [
    "TokenCreateView",
    "TokenDestroyView",
    "UserViewSet",
]


@extend_schema(tags=[SCHEMA_TAG_AUTH])
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


@extend_schema(tags=[SCHEMA_TAG_AUTH])
class TokenDestroyView(DjoserTokenDestroyView):
    def post(self, request):
        response = super().post(request)
        response.delete_cookie("auth_token")
        return response


@extend_schema(tags=[SCHEMA_TAG_AUTH])
class UserViewSet(DjoserUserViewSet):
    pass
