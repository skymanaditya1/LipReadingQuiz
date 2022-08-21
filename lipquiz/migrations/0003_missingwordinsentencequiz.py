# Generated by Django 3.2 on 2022-08-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lipquiz', '0002_videoquiz_is_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='MissingWordInSentenceQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=256)),
                ('number_of_questions', models.IntegerField()),
                ('time', models.IntegerField(help_text='Duration of the quiz')),
                ('difficulty', models.CharField(choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], max_length=6)),
                ('quiz_type', models.CharField(choices=[('single word mcq', 'single word mcq'), ('single word blank with context', 'single word blank with context'), ('sentence with context', 'sentence with context'), ('sentence with blank', 'sentence with blank')], max_length=120)),
                ('score_required_to_pass', models.IntegerField(help_text='Minimum score required to pass the quiz')),
                ('is_visible', models.BooleanField(default=False, help_text='Whether the quiz is visible or not')),
            ],
            options={
                'verbose_name_plural': 'MissingWordQuizzes',
            },
        ),
    ]
