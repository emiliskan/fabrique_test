from django.urls import path
from .views import PollView, UserPollsView

urlpatterns = [
    path('polls/', PollView.as_view()),
    path('polls/users/<int:user_id>', UserPollsView.as_view()),
]
