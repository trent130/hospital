# Generated by Django 5.0.1 on 2024-09-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0003_remove_appointment_prescription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'doc'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
