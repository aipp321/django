# Generated by Django 2.2.6 on 2019-10-24 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20191024_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bolgs',
            options={'ordering': ['-created_time']},
        ),
        migrations.AlterField(
            model_name='bolgs',
            name='author',
            field=models.ForeignKey(default='不知道', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]