from django.db import models
from autoslug.fields import AutoSlugField
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    image = models.ImageField(upload_to='home/category/', verbose_name='Kategori Fotosu:')
    name = models.CharField(max_length=20, verbose_name='Kategori')
    explain = models.TextField(verbose_name='Kategori Tanımı')
    slug = AutoSlugField(populate_from='name', unique=True)

    publish = models.DateTimeField(default=timezone.now, verbose_name='Yayınlama Tarihi')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategori'
