# Generated by Django 4.1.6 on 2023-04-05 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, verbose_name='카테고리 타입')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성 일시')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정 일시')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='삭제 여부')),
                ('title', models.CharField(max_length=255, verbose_name='설문 제목')),
                ('thumbnail', models.URLField(max_length=255, verbose_name='설문 썸네일')),
                ('data', models.JSONField(null=True, verbose_name='설문 데이터')),
                ('status', models.IntegerField(choices=[(0, 'idle'), (1, 'ongoing'), (2, 'done'), (3, 'awarded')], default=0, verbose_name='설문 상태')),
                ('is_survey_hidden', models.BooleanField(default=False, verbose_name='공개_비공개_여부')),
                ('end_at', models.DateTimeField(verbose_name='설문 종료 일시')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='survey.category', verbose_name='카테고리')),
            ],
            options={
                'verbose_name': 'Survey',
                'verbose_name_plural': 'Surveys',
                'db_table': 'survey',
            },
        ),
    ]
