# Generated by Django 3.2.5 on 2021-08-17 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybasic', '0005_topic_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='profession',
            field=models.CharField(choices=[('student', 'student'), ('developer', 'developer')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]