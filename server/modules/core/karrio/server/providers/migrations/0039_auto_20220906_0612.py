# Generated by Django 3.2.14 on 2022-09-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0038_alter_genericsettings_label_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uspsinternationalsettings',
            name='mailer_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='uspssettings',
            name='mailer_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]