# Generated by Django 4.0.2 on 2022-09-28 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turma', models.CharField(choices=[['2', '2AI'], ['2', '2B'], ['2', '2BI']], max_length=10, null=True)),
            ],
        ),
    ]
