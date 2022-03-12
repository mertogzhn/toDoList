from django.db import models
from django.utils import timezone
# Create your models here.


class ToDoList(models.Model):
    baslik =models.CharField(max_length=144,verbose_name="Başlik")
    aciklama = models.TextField(blank=True,null=True,verbose_name="Açiklama")
    eklenme_tarihi = models.DateTimeField(default=timezone.now,verbose_name="Eklenme Tarihi")
    durum = models.BooleanField(default=False,verbose_name="Yapildi")


    class Meta:
        verbose_name="Yapilacaklar"
        verbose_name_plural="Yapilacaklar"

    def __str__(self):
        return self.baslik