# Generated by Django 5.0.7 on 2024-08-04 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EditRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='docs')),
                ('description', models.TextField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('category', models.IntegerField(choices=[(1, 'Literature'), (2, 'Biography'), (3, 'Science'), (4, 'Physic'), (5, 'Math')])),
            ],
        ),
    ]
