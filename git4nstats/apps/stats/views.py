import logging

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK
)
from rest_framework.views import APIView

from utils.mixins import (
    ExceptionHandlerMixin,
)

from stats import services as stats_ser

logger = logging.getLogger(__name__)


class GitHubUsers(
    ExceptionHandlerMixin,
    APIView
):
    class InputSerializer(serializers.Serializer):
        github_users = serializers.ListField(
            child=serializers.CharField()
        )

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = stats_ser.find_github_users(
            **serializer.validated_data
        )

        return Response({'users': result}, HTTP_200_OK)
