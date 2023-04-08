# Generated by Django 4.1.7 on 2023-03-29 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='receptionistprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='bio',
        ),
        migrations.DeleteModel(
            name='DoctorProfile',
        ),
        migrations.DeleteModel(
            name='PatientProfile',
        ),
        migrations.DeleteModel(
            name='ReceptionistProfile',
        ),
    ]
