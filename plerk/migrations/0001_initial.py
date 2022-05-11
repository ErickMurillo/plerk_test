# Generated by Django 4.0.4 on 2022-05-10 20:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('status', models.IntegerField(choices=[(1, 'activa'), (0, 'inactiva')])),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('date_transaction', models.DateField()),
                ('status_transaction', models.CharField(choices=[('closed ', 'closed '), ('reversed ', 'reversed '), ('pending', 'pending')], max_length=10)),
                ('status_approved', models.BooleanField()),
                ('final_charge', models.BooleanField()),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plerk.empresa', verbose_name='Empresa')),
            ],
        ),
    ]
