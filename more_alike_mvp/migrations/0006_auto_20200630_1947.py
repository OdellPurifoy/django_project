# Generated by Django 3.0.7 on 2020-06-30 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('more_alike_mvp', '0005_auto_20200629_2309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='active',
            new_name='approved_comments',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='name',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
