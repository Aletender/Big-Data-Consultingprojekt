from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=200)
    tooltip = models.CharField(max_length=200)

    #return the question
    def __str__(self):
        return {"question": self.question, "tooltip": self.tooltip}

    @classmethod
    def create(cls, question, tooltip):
        return cls.objects.create(question=question, tooltip=tooltip)
