# Generated by Django 4.0.5 on 2022-06-23 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('message', models.TextField(max_length=30)),
                ('status', models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='New', max_length=10)),
                ('ip', models.CharField(blank=True, max_length=30)),
                ('note', models.CharField(blank=True, max_length=100)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]