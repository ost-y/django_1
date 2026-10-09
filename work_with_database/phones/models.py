from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField('name',max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:  # Если объект новый
            self.slug = slugify(self.name)  # Генерируем slug из поля name
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}, {self.price}, {self.image}'





# class Person(models.Model):
#     name = models.CharField(max_length=50)
#     car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='owners')


