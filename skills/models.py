from django.db import models


# model has same name as app only because it makes semantic sense in this case
class Skill(models.Model):
    # REQUIRES PILLOW maybe make images optional
    name = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.CharField(max_length=200)
    # maybe make this an FK
    difficulty = models.CharField(max_length=15, blank=True)
