# Generated by Django 4.2.1 on 2023-05-24 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='Номер телефона')),
                ('mobile_code', models.CharField(max_length=3, verbose_name='Код мобильного оператора')),
                ('tag', models.CharField(blank=True, max_length=50, verbose_name='Тег')),
                ('timezone', models.CharField(default='UTC', max_length=40, verbose_name='Часовой пояс')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_data', models.DateTimeField(verbose_name='Дата запуска рассылки')),
                ('end_data', models.DateTimeField(verbose_name='Дата окончания рассылки')),
                ('text', models.TextField(max_length=500, verbose_name='Текст')),
                ('tag', models.CharField(blank=True, max_length=50, verbose_name='Тег')),
                ('mobile_code', models.CharField(blank=True, max_length=3, verbose_name='Код мобильного оператора')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('sending_status', models.CharField(max_length=15, verbose_name='Статус')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.client')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.mailing')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]