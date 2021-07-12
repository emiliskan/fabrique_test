from polls.models import Poll


def get_active_polls() -> list[Poll]:
    """
    Список активных опросов
    :return:
    """
    return Poll.objects.all()
