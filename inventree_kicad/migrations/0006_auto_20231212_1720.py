# Generated by Django 3.2.20 on 2023-12-12 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventree_kicad', '0005_selectedcategory_default_value_parameter_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='selectedcategory',
            name='footprint_parameter_template',
            field=models.ForeignKey(blank=True, help_text='Footprint parameter template for this category, will use KICAD_FOOTPRINT_PARAMETER setting if not set', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='footprint_kicad_categories', to='part.partparametertemplate', verbose_name='Footprint Parameter Template'),
        ),
        migrations.CreateModel(
            name='FootprintParameterMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_value', models.CharField(max_length=200, verbose_name='Footprint Parameter Value')),
                ('kicad_footprint', models.CharField(max_length=200, verbose_name='KiCad Footprint')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventree_kicad.selectedcategory')),
            ],
            options={
                'verbose_name': 'Footprint Mapping',
                'unique_together': {('category', 'parameter_value')},
            },
        ),
    ]
