# Generated by Django 4.0.4 on 2022-05-10 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turnos', '0006_alter_turns_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turns',
            name='Staff',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turns',
            name='user',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
