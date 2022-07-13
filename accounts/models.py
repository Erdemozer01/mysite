from django.contrib.auth.models import User
from django.db import models
import uuid


class Profile(models.Model):
    Gender = [
        ('', '------'),
        ('Erkek', 'Erkek'),
        ('Kadın', 'Kadın'),
        ('Belirtmek istemiyorum', 'Belirtmek istemiyorum'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Kullanıcı Adı')
    cover = models.ImageField(upload_to='users/cover/', blank=True, verbose_name='Kapak Fotosu')
    avatar = models.ImageField(upload_to='users/avatar/', blank=True, verbose_name='Avatar')
    first_name = models.CharField(max_length=20, verbose_name='Adı')
    last_name = models.CharField(max_length=20, verbose_name='Soyadı')
    gender = models.CharField(max_length=30, choices=Gender, default="", verbose_name='Cinsiyet')
    address = models.TextField(verbose_name='Adres')
    location = models.CharField(max_length=100, verbose_name='Yaşadığı şehir', blank=True)
    email = models.EmailField(verbose_name='Email')
    about = models.TextField(verbose_name='Hakkımda', blank=True)
    job = models.CharField(max_length=100, verbose_name='Meslek', blank=True)
    phone = models.CharField(max_length=13, verbose_name='Telefon', blank=True)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Doğum Tarihi:')
    skils = models.CharField(max_length=200, editable=True, verbose_name='Yetenekler', blank=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)

    facebook = models.URLField(verbose_name='Facebook', blank=True)
    twitter = models.URLField(verbose_name='Twitter', blank=True)
    instagram = models.URLField(verbose_name='İnstagram', blank=True)

    created = models.DateTimeField(auto_now=True, verbose_name='Katılma Tarihi')

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'accounts'
        verbose_name = 'Profil'
        verbose_name_plural = 'Profil'
