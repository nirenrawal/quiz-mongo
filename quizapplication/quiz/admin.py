from django.contrib import admin
from .models import Question, QuizCategory, Answer, UserScore


admin.site.register(Question)
admin.site.register(QuizCategory)
admin.site.register(Answer)
admin.site.register(UserScore)


