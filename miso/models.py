from django.db import models
from django.utils import timezone

class Word(models.Model):
    word = models.CharField(max_length=10, null=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.word+" at "+str(self.date)
        # return self.word
