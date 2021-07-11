from django.contrib import admin
from .models import Poll, Question, PoolQuestion, UserPoll, UserPollAnswer


class PoolQuestionInline(admin.TabularInline):
    model = PoolQuestion
    extra = 0


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date")

    # порядок следования полей в форме создания/редактирования
    fields = ("name", "start_date", "end_date")
    search_fields = ("name",)
    readonly_fields = ("start_date", )
    inlines = [PoolQuestionInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "answer_type")


class UserPollAnswerInline(admin.TabularInline):
    model = UserPollAnswer
    extra = 0


@admin.register(UserPoll)
class UserPollAdmin(admin.ModelAdmin):
    list_display = ("poll", "user_id")
    inlines = [UserPollAnswerInline]
