from django.db import models

# Create your models here.
class Question(models.Model):
    content=models.CharField(max_length=1024)
    
    def __str__(self):
        return self.content
class Choices(models.Model):
    questions=models.ForeignKey('Question',on_delete=models.CASCADE)
    content=models.CharField(max_length=256)
    
    def __str__(self):
        return "{} - {}" .format(self.questions.content[:50], self.content)
