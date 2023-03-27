# Generated by Django 4.1.6 on 2023-03-26 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gifticon', '0001_initial'),
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gifticon',
            name='survey_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.survey', verbose_name='설문 ID'),
        ),
    ]
