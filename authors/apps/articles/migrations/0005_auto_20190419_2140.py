# Generated by Django 2.1.7 on 2019-04-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190419_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likesdislikesmodel',
            name='dislikes',
        ),
        migrations.AlterField(
            model_name='likesdislikesmodel',
            name='likes',
            field=models.BooleanField(default=False, null=True),
        ),
    ]