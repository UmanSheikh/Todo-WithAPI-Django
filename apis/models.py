from django.db import models


# Create your models here.
class TodoList(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.CharField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.status)


