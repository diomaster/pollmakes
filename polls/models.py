from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length = 255)
    pub_date = models.DateTimeField('Date Created')

    def __str__(self):
        return self.question_text
    
    
class Choice(models.Model):
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
