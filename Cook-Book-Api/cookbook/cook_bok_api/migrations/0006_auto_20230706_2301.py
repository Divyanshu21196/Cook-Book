# Generated by Django 2.2 on 2023-07-06 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cook_bok_api', '0005_auto_20230706_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipemenu',
            old_name='user_role_profile',
            new_name='user_role',
        ),
    ]
