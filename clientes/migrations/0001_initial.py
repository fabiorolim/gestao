# Generated by Django 2.1.3 on 2018-11-26 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=12)),
                ('bio', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='clients_photos')),
            ],
            options={
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]