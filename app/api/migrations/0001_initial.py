# Generated by Django 4.1.7 on 2024-01-15 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
                ('calories', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Testing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=55)),
                ('imagePath', models.CharField(max_length=55)),
                ('name', models.CharField(max_length=55)),
                ('products', models.ManyToManyField(related_name='testings', to='api.foodproduct')),
            ],
        ),
    ]