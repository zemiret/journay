# Generated by Django 2.1.7 on 2019-03-11 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190311_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayentry',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='journey',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
