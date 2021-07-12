from rest_framework.views import APIView
from rest_framework.response import Response

from polls.services.pool import get_active_polls
from polls.serializers.pool import PollSerializer


class PollView(APIView):
    """ Опросы """

    def get(self, request, format=None):
        """ Список опросов """
        polls = get_active_polls()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)
