# Generated by Django 2.1.5 on 2020-07-20 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('via', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traveler.Location'),
        ),
    ]
