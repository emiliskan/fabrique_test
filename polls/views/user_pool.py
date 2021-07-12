from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from polls.services.user_poll import get_user_pools
from polls.serializers.user_pool import UserPollSerializer


class UserPollsView(APIView):
    """ Опросы пользователя """

    def get(self, request, user_id, format=None):
        """ Получить список опросов пользователя """
        user_polls = get_user_pools(user_id)
        serializer = UserPollSerializer(user_polls, many=True)
        return Response(serializer.data)

    def post(self, request, user_id, format=None) -> Response:
        """ Добавить опрос пользователя """
        data = request.data
        data["user_id"] = user_id
        serializer = UserPollSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
