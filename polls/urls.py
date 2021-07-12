from django.urls import path
from polls.views.pool import PollView
from polls.views.user_pool import UserPollsView

urlpatterns = [
    path('polls/', PollView.as_view()),
    path('polls/users/<int:user_id>', UserPollsView.as_view()),
]
