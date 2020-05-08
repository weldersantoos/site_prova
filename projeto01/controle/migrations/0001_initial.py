# Generated by Django 3.0.5 on 2020-05-08 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('cidade', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('Telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('horario_data_criacao', models.DateTimeField(auto_now_add=True)),
                ('foto', models.ImageField(upload_to='')),
                ('ativo', models.BooleanField(default=True)),
                ('nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]