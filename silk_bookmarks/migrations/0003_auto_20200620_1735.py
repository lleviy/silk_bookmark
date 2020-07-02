# Generated by Django 2.2.6 on 2020-06-20 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('silk_bookmarks', '0002_topic_photo_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'quotes',
            },
        ),
        migrations.RenameModel(
            old_name='Topic',
            new_name='Book',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.AddField(
            model_name='quote',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='silk_bookmarks.Book'),
        ),
    ]
