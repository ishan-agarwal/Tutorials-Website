from django.contrib import admin
from .models import Tutorial, Question
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
    fields = ["tutorial_title",
              "tutorial_content",
              ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


class QuestionAdmin(admin.ModelAdmin):
    fields = ["question",
              "option_1",
              "option_2",
              "option_3",
              "option_4",
              "correct_option",
              "tutorial_it_belongs_to",
              ]


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Question, QuestionAdmin)
