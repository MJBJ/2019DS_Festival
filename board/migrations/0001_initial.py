# Generated by Django 2.1.7 on 2019-05-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
                ('Title', models.CharField(blank=True, max_length=20)),
                ('Text', models.TextField(blank=True, max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pwd', models.CharField(default='0000', max_length=10)),
            ],
        ),
    ]