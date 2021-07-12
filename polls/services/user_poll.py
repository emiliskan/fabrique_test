from polls.models import UserPoll, AnswerQuestion, UserPollAnswer, PoolQuestion, Question


class QuestionNotInPool(Exception):
    """Base class for exceptions in this module."""

    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)


def get_user_pools(user_id: str) -> list[UserPoll]:
    """
    Получить список опросов пользователя
    :param user_id: идентификатор пользователя
    :return: список опросов
    """
    return UserPoll.objects.filter(user_id__exact=user_id).all()


def create_user_pool(data: dict) -> UserPoll:
    """
    Создание опроса и добавление ответов в него
    :param data: Данные для создания объекта
    :return: Созданный объект
    """
    user_answers = data.pop('answers')
    user_poll = UserPoll.objects.create(**data)

    for answer in user_answers:
        answer_question = create_answer_question(answer['question'], answer['answer'])
        create_user_pool_answer(user_poll, answer_question)

    return user_poll


def create_answer_question(question: Question, answer: str) -> AnswerQuestion:
    """
    Сохранить ответ на вопрос
    :param question: Объект модели вопроса
    :param answer: Ответ
    :return: Созданный объект
    """
    return AnswerQuestion.objects.create(question=question, answer=answer)


def create_user_pool_answer(user_poll: UserPoll, answer_question: AnswerQuestion) -> UserPollAnswer:
    """
    Привязать ответ на вопрос к опросу пользователя
    :param user_poll: Опрос пользователя
    :param answer_question: Объект модели ответа на вопрос
    :return: Ответ на вопрос в опросе
    """
    return UserPollAnswer.objects.create(user_poll=user_poll, answer_question=answer_question)
