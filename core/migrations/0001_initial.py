# Generated by Django 2.2.7 on 2019-11-07 14:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original', models.ImageField(blank=True, null=True, upload_to='galeria/original')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='galeria/thumbnail')),
                ('publicacao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Album')),
            ],
        ),
    ]
