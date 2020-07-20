# Generated by Django 3.0.8 on 2020-07-17 21:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
                ('birthdate', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(4000)])),
                ('terms', models.IntegerField()),
                ('income', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=15)),
                ('result', models.CharField(max_length=15, null=True)),
                ('refused_policy', models.CharField(default='', max_length=15, null=True)),
                ('amount', models.FloatField(null=True)),
                ('terms', models.IntegerField(null=True)),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Loan')),
            ],
        ),
    ]