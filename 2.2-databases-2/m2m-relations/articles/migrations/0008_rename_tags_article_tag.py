# Generated by Django 4.2.6 on 2023-10-17 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_remove_article_scopes_article_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='tag',
        ),
    ]