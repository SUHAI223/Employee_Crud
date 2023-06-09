# Generated by Django 4.1.7 on 2023-04-02 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='userapp/static/')),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.designation')),
            ],
        ),
    ]
