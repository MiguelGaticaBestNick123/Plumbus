# Generated by Django 4.2.2 on 2023-07-07 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_contacto_alter_carrito_id_alter_formulariopago_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='asunto',
            field=models.CharField(default='n/a', max_length=80),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='num_telefono',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
