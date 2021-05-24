# Generated by Django 3.2 on 2021-05-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210524_2027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age_hearing_loss',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='hearing_loss_age',
            field=models.IntegerField(default=None, help_text='Age at which hearing loss occurred', null=True),
        ),
    ]