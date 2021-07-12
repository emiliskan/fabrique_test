from django.db import models
from django.utils.translation import gettext_lazy as _

ANSWER_TYPES = [
    ("TEXT", _('ответ текстом')),
    ("SINGLE_CHOICE", _('выбор одного варианта')),
    ("MULTIPLY_CHOICE", _('выбор нескольких вариантов'))
]


class Poll(models.Model):
    """ Опросы """
    name = models.CharField(max_length=250)
    start_date = models.DateField(_("дата начала"), auto_now=True)
    end_date = models.DateField(_("дата окончания"), null=True, blank=True)

    questions = models.ManyToManyField('Question', through='PoolQuestion')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('опрос')
        verbose_name_plural = _('опросы')


class Question(models.Model):
    """ Вопросы для опросов """
    text = models.TextField()
    answer_type = models.CharField(
        _("Тип ответа"),
        max_length=250,
        choices=ANSWER_TYPES,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = _('вопрос')
        verbose_name_plural = _('вопросы')


class PoolQuestion(models.Model):
    """ Вопросы опроса """
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}'

    class Meta:
        verbose_name = _('вопрос опроса')
        verbose_name_plural = _('вопросы опросов')


class UserPoll(models.Model):
    """ Опросы пользователей """
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    answers = models.ManyToManyField('AnswerQuestion', through='UserPollAnswer')

    def __str__(self):
        return f'{self.user_id}'

    class Meta:
        verbose_name = _('опрос пользователя')
        verbose_name_plural = _('опросы пользователей')


class AnswerQuestion(models.Model):
    """ Ответы на вопросы """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return f'{self.question} {self.answer}'

    class Meta:
        verbose_name = _('ответ на вопрос')
        verbose_name_plural = _('ответы на вопросы')


class UserPollAnswer(models.Model):
    """ Связка опросов пользователей с ответами на вопросы """
    answer_question = models.ForeignKey(AnswerQuestion, on_delete=models.CASCADE)
    user_poll = models.ForeignKey(UserPoll, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.answer_question}'

    class Meta:
        verbose_name = _('ответ на вопрос опроса')
        verbose_name_plural = _('ответы на вопросы опросов')
