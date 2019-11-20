# Generated by Django 2.2.1 on 2019-10-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='Pics')),
                ('desc', models.TextField(max_length=500)),
                ('price', models.IntegerField(max_length=10)),
            ],
        ),
    ]