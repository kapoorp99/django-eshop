# Generated by Django 3.0.9 on 2020-08-29 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]