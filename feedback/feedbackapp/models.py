from django.db import models
class feedbackmodel(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    tutorname=models.CharField(max_length=100,null=True,blank=True)
    feedback12=models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        db_table='feedback'
