from django.db import models



# Create your models here.
class TestModel(models.Model):
    a = models.IntegerField('a')
    b = models.IntegerField('b')
    c = models.IntegerField('c')

    def __str__(self):
        return f'a: {self.a} b: {self.b} c: {self.c}'





