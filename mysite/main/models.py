from django.db import models
from tinymce import models as tinymce_models
from tinymce.models import HTMLField


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()

    def __str__(self):
        return self.tutorial_title


class Question(models.Model):
    question = models.TextField()
    option_1 = models.CharField(max_length=200)
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)
    correct_option = models.IntegerField()
    tutorial_it_belongs_to = models.ForeignKey(
        Tutorial, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
