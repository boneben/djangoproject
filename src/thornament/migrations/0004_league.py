# Generated by Django 3.0.3 on 2020-02-28 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thornament', '0003_auto_20200225_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_name', models.CharField(max_length=200, null=True)),
                ('league_type', models.CharField(choices=[('One time', 'One time'), ('Two times', 'Two times'), ('Three times', 'Three times')], max_length=200, null=True)),
                ('league_teams', models.IntegerField(null=True)),
                ('league_seed', models.BooleanField(default=False, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
