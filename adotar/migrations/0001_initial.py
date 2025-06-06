# Generated by Django 5.1.2 on 2024-10-27 00:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('divulgar', '0004_alter_pet_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoAdocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('status', models.CharField(choices=[('AG', 'Aguardando Aprovação'), ('AP', 'Aguardando Aprovação'), ('R', 'Aguardando Aprovação')], default='AG', max_length=2)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='divulgar.pet')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
