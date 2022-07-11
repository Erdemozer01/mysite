# Generated by Django 4.0.6 on 2022-07-11 17:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_terms_alter_cover_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bottom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Anasayfa', max_length=100, verbose_name='Başlık')),
                ('text', models.TextField(verbose_name='İçerik')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Yayınlama Tarihi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
            ],
            options={
                'verbose_name': 'Alt Kapak',
                'verbose_name_plural': 'Alt Kapak',
                'db_table': 'bottom_cover',
                'ordering': ['publish'],
            },
        ),
    ]
