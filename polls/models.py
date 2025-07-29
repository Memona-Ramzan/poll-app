from django.db import models

# Create your models here.
# inheriting the feature of models like models.model
class Question(models.Model):
    Question_field=models.CharField(max_length=100)
class Choices(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name="choices")
    # That tells Django each Choice is related to a single Question
    # If you delete the Question, Django will also delete all the related Choices 
    # automatically — because of models.CASCADE.
    choices_field=models.CharField(max_length=10)
    votes=models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.question} {self.choices_field}"
    