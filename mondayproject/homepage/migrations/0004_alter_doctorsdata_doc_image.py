# Generated by Django 5.0 on 2023-12-24 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_rename_doctors_doctorsdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorsdata',
            name='doc_image',
            field=models.ImageField(upload_to='doctorsData'),
        ),
    ]
