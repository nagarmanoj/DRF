from django.db import models

# Create your models here.

class Question(models.Model):
    questions = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice
