from polls.models import UserPoll, AnswerQuestion
from rest_framework import serializers
from polls.services.user_poll import create_user_pool


class AnswerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestion
        fields = ['id', 'question', 'answer']


class UserPollSerializer(serializers.ModelSerializer):
    answers = AnswerQuestionSerializer(many=True)

    def create(self, validated_data: dict) -> UserPoll:
        """
        DRF не умеет сереализовывать nested поля, поэтому надо вручную добавить answers
        :param validated_data: Данные для создания опроса пользователя
        :return: Созданный опрос пользователя
        """
        return create_user_pool(validated_data)

    class Meta:
        model = UserPoll
        fields = ['poll', 'user_id', 'answers']
