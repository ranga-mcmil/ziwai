# Generated by Django 4.1.7 on 2023-03-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_payment_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], default='Not Paid', max_length=10),
        ),
    ]
