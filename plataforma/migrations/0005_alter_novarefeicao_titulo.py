# Generated by Django 4.1.1 on 2022-10-31 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0004_remove_opcao_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novarefeicao',
            name='titulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plataforma.refeicao'),
        ),
    ]
