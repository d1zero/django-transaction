from django.db import models

class Book(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "books"
