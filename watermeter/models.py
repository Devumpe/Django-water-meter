from django.db import models

# Create your models here.
class Watermeter_Table(models.Model):
    roomid = models.CharField(max_length=255)
    # imagemeter = models.ImageField(upload_to=get_image_path, blank=True, null=True)  
    date = models.IntegerField()
