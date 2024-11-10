from django.db import models

# Create your models here.

class Title(models.Model):
    title = models.CharField(max_length=50)

    

    class Meta:
        verbose_name = "Title"
        verbose_name_plural = "Titles"

    def __str__(self):
        return self.title

    
class Choice(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='choice')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    
    class Meta:
        verbose_name = "Choice"
        verbose_name_plural = "Choices"

