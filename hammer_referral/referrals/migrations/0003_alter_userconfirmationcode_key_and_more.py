# Generated by Django 4.2.3 on 2023-08-19 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0002_userconfirmationcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userconfirmationcode',
            name='key',
            field=models.CharField(max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='userconfirmationcode',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.CreateModel(
            name='Referring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referral', to=settings.AUTH_USER_MODEL, verbose_name='приглашенный пользователь')),
                ('referrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrer', to=settings.AUTH_USER_MODEL, verbose_name='пригласивший пользователь')),
            ],
        ),
    ]
