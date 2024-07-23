# Generated by Django 5.0.7 on 2024-07-21 17:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('habits', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='habit',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action', to='habits.action', verbose_name='Действие'),
        ),
        migrations.AddField(
            model_name='habit',
            name='award',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='award', to='habits.action', verbose_name='Вознаграждение'),
        ),
        migrations.AddField(
            model_name='habit',
            name='link_action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link_action', to='habits.action', verbose_name='Связанная привычка'),
        ),
        migrations.AddField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
