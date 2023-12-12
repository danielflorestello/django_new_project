# Generated by Django 4.2.4 on 2023-11-30 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_detallerecomendacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.servicio')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.tipo')),
            ],
        ),
        migrations.RemoveField(
            model_name='detallerecomendacion',
            name='cantidad_devuelta',
        ),
        migrations.CreateModel(
            name='DetalleCaso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('cantidad_devuelta', models.IntegerField(default=0)),
                ('caso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.caso')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.equipo')),
            ],
        ),
    ]