# Generated by Django 4.2.2 on 2023-07-09 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_review_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ratingClass',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='ratingMaterial',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='ratingOrganization',
            field=models.IntegerField(),
        ),
    ]