# Generated by Django 3.2.3 on 2021-10-09 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
