from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='имя'
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    is_active = models.BooleanField(
        verbose_name='активна',
        default=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='имя товара',
        max_length=128,
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True,
    )
    short_desc = models.CharField(
        verbose_name='краткое описание',
        max_length=60,
        blank=True
    )
    description = models.TextField(
        verbose_name='название товара',
        blank=True,
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество товара на кладе',
        default=0,
    )
    is_active = models.BooleanField(
        verbose_name='активна',
        default=True
    )

    def __str__(self):
        return f'{self.name} ({self.category.name})'
