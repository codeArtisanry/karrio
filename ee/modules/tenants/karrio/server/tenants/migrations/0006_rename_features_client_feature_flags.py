# Generated by Django 3.2.14 on 2022-08-30 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0005_remove_client_feature_flags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='features',
            new_name='feature_flags',
        ),
    ]