# Generated by Django 3.2.3 on 2021-06-09 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_comment_recipe'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'コメント', 'verbose_name_plural': 'コメント'},
        ),
    ]
