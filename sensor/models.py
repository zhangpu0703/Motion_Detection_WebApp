from django.db import models

# Create your models here.
class motion_detect(models.Model):
    reading=models.CharField(max_length=200)
    time=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.reading

class duration(models.Model):
    reading=models.CharField(max_length=20)
    time=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.reading

class normalize(models.Model):
    reading=models.CharField(max_length=20)
    time=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.reading
