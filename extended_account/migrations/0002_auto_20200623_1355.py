# Generated by Django 2.2.6 on 2020-06-23 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_update_default_language'),
        ('extended_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.Account')),
                ('photo_url', models.URLField(blank=True)),
                ('colour', models.CharField(blank=True, max_length=50)),
            ],
            bases=('account.account',),
        ),
        migrations.DeleteModel(
            name='Appearance',
        ),
    ]
