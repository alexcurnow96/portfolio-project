# Generated by Django 4.2.16 on 2024-09-30 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['completed']},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='completed',
        ),
    ]
