# Generated by Django 5.0.1 on 2024-02-13 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialsTable',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.DecimalField(decimal_places=0, max_digits=10)),
                ('country', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'credentials_table',
            },
        ),
    ]
