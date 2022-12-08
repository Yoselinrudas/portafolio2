# Generated by Django 4.1.4 on 2022-12-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('title_proj', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=80)),
                ('tags', models.CharField(max_length=50)),
                ('url_git', models.URLField(blank=True)),
            ],
        ),
    ]