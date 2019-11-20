# Generated by Django 2.2.4 on 2019-11-13 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_auto_20191108_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderInfrastructureMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infrastructure_type', models.CharField(choices=[('AWS', 'AWS'), ('AZURE', 'AZURE'), ('GCP', 'GCP'), ('AWS-local', 'AWS-local'), ('AZURE-local', 'AZURE-local'), ('GCP-local', 'GCP-local')], max_length=50)),
                ('infrastructure_provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Provider')),
            ],
        ),
        migrations.AddField(
            model_name='provider',
            name='infrastructure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.ProviderInfrastructureMap'),
        ),
    ]