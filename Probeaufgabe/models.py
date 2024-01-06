from django.db import models


# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=80)
    semester = models.IntegerField()
    start_date = models.DateField()
    average = models.DecimalField(max_digits=3, decimal_places=1)
