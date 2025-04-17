# Generated by Django 5.2 on 2025-04-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terms', '0003_alter_term_options_term_first_letter_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='term',
            options={'ordering': ['term_name']},
        ),
        migrations.RemoveField(
            model_name='term',
            name='first_letter',
        ),
        migrations.AlterField(
            model_name='term',
            name='term_description',
            field=models.TextField(verbose_name='Описание термина'),
        ),
        migrations.AlterField(
            model_name='term',
            name='term_name',
            field=models.CharField(max_length=200, verbose_name='Название термина'),
        ),
    ]
