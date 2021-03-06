# Generated by Django 3.1.2 on 2020-11-09 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComments',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
