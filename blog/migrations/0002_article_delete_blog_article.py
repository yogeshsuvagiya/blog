# Generated by Django 4.0.5 on 2022-07-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='blog_images')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='blog_article',
        ),
    ]
