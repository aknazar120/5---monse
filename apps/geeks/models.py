from django.db import models # type: ignore

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    ingredients = models.TextField(verbose_name="Ингредиенты")
    instructions = models.TextField(verbose_name="Инструкция")
    preparation_time = models.PositiveIntegerField(verbose_name="Время приготовления (минуты)")
    is_vegetarian = models.BooleanField(default=False, verbose_name="Вегетарианский")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title