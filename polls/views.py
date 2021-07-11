from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from polls.models import Poll, UserPoll
from polls.serializers import PollSerializer, UserPollSerializer


class PollView(APIView):
    """ Список опросов """
    def get(self, request, format=None):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)


class UserPollsView(APIView):
    """ Опросы пользователя """
    serializer = UserPollSerializer

    def get(self, request, user_id, format=None):
        """ Получить список опросов пользователя """
        user_polls = UserPoll.objects.filter(user_id__exact=user_id).all()
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
