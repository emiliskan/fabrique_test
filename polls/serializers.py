from polls.models import Poll, Question, UserPoll, UserPollAnswer, AnswerQuestion
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'answer_type']


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = ['id', 'name', 'questions']


class AnswerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestion
        fields = ['id', 'question', 'answer']


class UserPollSerializer(serializers.ModelSerializer):
    answers = AnswerQuestionSerializer(many=True)

    def create(self, validated_data: dict) -> UserPoll:
        """ Создание опроса и добавление отетов в него """
        answers = validated_data.pop('answers')
        user_poll = UserPoll.objects.create(**validated_data)

        # DRF не умеет сереализовывать nested поля, поэтому надо вручную
        for answer in answers:
            answer_question = AnswerQuestion(question=answer['question'], answer=answer['answer'])
            answer_question.save()
            UserPollAnswer.objects.create(user_poll=user_poll, answer_question=answer_question)

        return user_poll

    class Meta:
        model = UserPoll
        fields = ['poll', 'user_id', 'answers']
