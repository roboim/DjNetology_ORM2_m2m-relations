# Generated by Django 4.2.6 on 2023-10-17 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_scope_article_alter_scope_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
    ]
