# Generated by Django 4.1.3 on 2022-11-07 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_done', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=255)),
                ('deadline', models.DateField()),
                ('todolist_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.todolist')),
            ],
        ),
    ]
