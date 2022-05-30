from django.db import models

# Create your models here.
class Entry(models.Model):
    text = models.TextField()

    #save date as it's created
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)
