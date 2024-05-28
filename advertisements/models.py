from django.db import models

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=32)
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=True)
    city = models.CharField(null=True, max_length=16)

    def __str__(self) -> str:
        return f"{self.title} {self.price} USD"

