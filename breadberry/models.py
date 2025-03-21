from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(verbose_name='Фотография', **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Position(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', **NULLABLE)
    price = models.FloatField(verbose_name='Цена')
    image = models.ImageField(verbose_name='Фотография', **NULLABLE)

    def __str__(self):
        return f"{self.title}, {self.description}, {self.category}"

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'
