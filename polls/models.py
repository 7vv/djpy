from django.db import models
from django.utils import timezone

class Queseion(models.Model):
    questionText = models.CharField(max_length = 200)
    publishDate = models.DateTimeField('date published')

    # object expression
    def __str__(self):
        return self.questionText
    
    # def was_published_recently(self):
    #     return self.publishDate >= timezone.now() - datetime.timedelta(days=1)    

class Choice(models.Model):
    questionText = models.ForeignKey(Queseion, on_delete=models.CASCADE)
    chioceText = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    
    # object expression
    def __str__(self):
        return self.chioceText