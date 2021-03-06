# Generated by Django 2.2.12 on 2020-05-10 20:32

from django.db import migrations, models
import djongo.models.fields
import facts.models


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=4096)),
                ('name', models.CharField(max_length=4096)),
                ('location', djongo.models.fields.EmbeddedField(model_container=facts.models.MultiPolygon, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='person',
            name='type',
            field=models.CharField(default='None', max_length=4096),
            preserve_default=False,
        ),
    ]
