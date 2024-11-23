from django.db import models


class Movie(models.Model):
    class Genre(models.TextChoices):
        HORROR = 'hr', 'Хоррор'
        ACTION = 'ac', 'Экшн'
        FANTASTIC = 'fa', 'Фантастика'
        SCIENTIFIC = 'sc', 'Научный'
        
    
    name = models.CharField(max_length=255, verbose_name="Название")
    genre = models.CharField(max_length=255, choices=Genre.choices, verbose_name="Жанр")
    year = models.IntegerField(verbose_name="Год выпуска")
    description = models.TextField(verbose_name="Описание")
    duration = models.CharField(max_length=255, verbose_name="Продолжительность")

    def __str__(self) -> str:
        return f'{self.name}({self.year}) - {self.get_genre_display()}'
