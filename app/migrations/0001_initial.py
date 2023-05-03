# Generated by Django 4.2 on 2023-05-03 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('species', models.CharField(choices=[('Собака', 'Собака'), ('Кошка', 'Кошка')], max_length=20)),
                ('gender', models.CharField(choices=[('Мальчик', 'Мальчик'), ('Девочка', 'Девочка')], max_length=10, verbose_name='Пол')),
                ('short_text', models.CharField(max_length=255, verbose_name='Короткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('main_image', models.ImageField(upload_to='animal_images', verbose_name='Главное изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя волонтера')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='AnimalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='animal_images', verbose_name='Изображение животного')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.animal')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='caretaker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.volunteer'),
        ),
    ]
