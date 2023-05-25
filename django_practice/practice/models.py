from django.db import models

# Create your models here.
class Visitor(models.Model):
    Name = models.TextField("")
    title = models.TextField(default="guest")
    last_come_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "visitor"