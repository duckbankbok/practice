from django.db import models

# Create your models here.
class visit(models.Model):
    visitor = models.CharField(max_length=100)
    pub_date = models.DateTimeField("date published")
    body = models.TextField()

    def __str__(self):
        return self.visitor

    def summary(self):
        return self.body[:20]
