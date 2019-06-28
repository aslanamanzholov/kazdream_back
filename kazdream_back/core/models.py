from django.db import models

class Tasks(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Время создания задачи')

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Время создания тэга')
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return self.name