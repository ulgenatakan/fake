# Generated by Django 2.2.6 on 2019-10-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_delete_testmodel2'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_field', models.IntegerField(blank=True)),
                ('x', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'test_model2',
                'managed': False,
            },
        ),
    ]
