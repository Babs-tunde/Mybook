from django.db import models

from django.db import models

class BookInfo(models.Model):
    ISBN = models.BigIntegerField(unique=True)
    book_title = models.CharField(max_length=255)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=255)
    author_origin = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    published_date = models.DateField()
    date_received = models.DateField()
    number_of_pages = models.IntegerField()

    def __str__(self):
        return self.book_title

