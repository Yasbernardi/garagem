# Generated by Django 4.0.5 on 2022-08-18 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descricao',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('ano', models.IntegerField(blank=True, null=True)),
                ('cor', models.CharField(blank=True, max_length=50, null=True)),
                ('preco', models.FloatField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='carros', to='core.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='carros', to='core.marca')),
            ],
        ),
    ]
