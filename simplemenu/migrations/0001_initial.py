# Generated by Django 2.1.4 on 2018-12-29 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Caption')),
                ('urlstr', models.CharField(max_length=255)),
                ('is_valid', models.BooleanField(default=False)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simplemenu.Menu')),
            ],
            options={
                'verbose_name': 'menu item',
                'verbose_name_plural': 'menu items',
            },
        ),
        migrations.CreateModel(
            name='URLItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Caption')),
                ('url', models.CharField(max_length=255)),
            ],
        ),
    ]