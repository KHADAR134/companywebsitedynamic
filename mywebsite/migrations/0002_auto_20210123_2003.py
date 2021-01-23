# Generated by Django 3.1.1 on 2021-01-23 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='photos/')),
            ],
        ),
        migrations.DeleteModel(
            name='products',
        ),
        migrations.AlterField(
            model_name='people',
            name='photo',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
