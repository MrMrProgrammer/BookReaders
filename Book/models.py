from django.db import models


# Create your models here.

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=100)
    publisher_logo = models.ImageField(upload_to='publisher_logo')


class Genre(models.Model):
    genre = models.CharField(max_length=100)


class Book(models.Model):
    fa_book_name = models.CharField(max_length=100, blank=True)
    en_book_name = models.CharField(max_length=100, blank=True)
    writer = models.CharField(max_length=100)
    translator = models.CharField(max_length=100)
    book_genre = models.ManyToManyField(Genre)
    book_publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, blank=True)
    book_photo = models.ImageField(upload_to='book_photo')
    read_count = models.IntegerField(default=0)
    reading_count = models.IntegerField(default=0)
    summary = models.TextField()

    def __str__(self):
        if self.fa_book_name:
            name = self.fa_book_name
        else:
            name = self.en_book_name

        return str(name)

    class Meta:
        db_table = 'Book'
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'