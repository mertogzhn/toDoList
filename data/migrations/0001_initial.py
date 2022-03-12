# Generated by Django 4.0.3 on 2022-03-12 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=144, verbose_name='Başlik')),
                ('aciklama', models.TextField(blank=True, null=True, verbose_name='Açiklama')),
                ('eklenme_tarihi', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Eklenme Tarihi')),
                ('durum', models.BooleanField(default=False, verbose_name='Yapildi')),
            ],
            options={
                'verbose_name': 'Yapilacaklar',
                'verbose_name_plural': 'Yapilacaklar',
            },
        ),
    ]
