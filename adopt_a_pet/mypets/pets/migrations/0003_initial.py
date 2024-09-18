# Generated by Django 5.1.1 on 2024-09-12 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0002_delete_animal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('especie', models.CharField(max_length=50)),
                ('edad', models.PositiveIntegerField()),
                ('fecha_ingreso', models.DateField()),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
