# Generated by Django 5.1.7 on 2025-03-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoilData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depth', models.FloatField(help_text='Depth in meters')),
                ('unit_weight', models.FloatField(help_text='Unit weight in kN/m3')),
                ('measured', models.IntegerField(help_text='Measured (N) value')),
                ('soil_type', models.CharField(choices=[('s', 'Sand/Nonplastic Silt'), ('c', 'Silt/Clay')], help_text='Soil Type', max_length=1)),
                ('uscs_classification', models.CharField(help_text='USCS Classification', max_length=20)),
                ('fc', models.FloatField(help_text='Fine Content (FC%)')),
                ('er', models.FloatField(help_text='Energy Ratio (ER%)')),
                ('peak_ground_acceleration', models.FloatField(help_text='Peak Ground Acceleration (g)')),
                ('earthquake_magnitude', models.FloatField(help_text='Earthquake Magnitude (M)')),
                ('water_table_depth', models.FloatField(help_text='Water Table Depth (m)')),
                ('borehole_diameter', models.FloatField(help_text='Borehole Diameter (mm)')),
                ('requires_correction_sampler_liners', models.BooleanField(help_text='Requires Correction for Sampler Liners (Yes/No)')),
                ('rod_length', models.FloatField(help_text='Rod Length (depth + 1.5m)')),
                ('ce', models.FloatField(blank=True, editable=False, null=True)),
                ('cb', models.FloatField(blank=True, editable=False, null=True)),
                ('cr', models.FloatField(blank=True, editable=False, null=True)),
                ('initial_cs', models.FloatField(blank=True, editable=False, null=True)),
                ('mid_cs', models.FloatField(blank=True, editable=False, null=True)),
                ('final_cs', models.FloatField(blank=True, editable=False, null=True)),
                ('initial_n60', models.FloatField(blank=True, editable=False, null=True)),
                ('mid_n60', models.FloatField(blank=True, editable=False, null=True)),
                ('final_n60', models.FloatField(blank=True, editable=False, null=True)),
                ('incremental_total_stress', models.FloatField(blank=True, editable=False, help_text='Incremental total stress (kPa)', null=True)),
                ('svc', models.FloatField(blank=True, editable=False, help_text='Total vertical stress (svc) (kPa)', null=True)),
                ('svc_prime', models.FloatField(blank=True, editable=False, help_text="Effective vertical stress (s'vc) (kPa)", null=True)),
                ('cn', models.FloatField(blank=True, editable=False, null=True)),
                ('initial_n1_60', models.FloatField(blank=True, editable=False, null=True)),
                ('mid_n1_60', models.FloatField(blank=True, editable=False, null=True)),
                ('final_n1_60', models.FloatField(blank=True, editable=False, null=True)),
                ('dr', models.FloatField(blank=True, editable=False, null=True)),
                ('adjusted_fc', models.FloatField(blank=True, editable=False, null=True)),
                ('f', models.FloatField(blank=True, editable=False, null=True)),
                ('v_s', models.FloatField(blank=True, editable=False, null=True)),
                ('rd', models.FloatField(blank=True, editable=False, null=True)),
                ('csr', models.FloatField(blank=True, editable=False, null=True)),
                ('dwfm_sand', models.FloatField(blank=True, editable=False, null=True)),
                ('ks', models.FloatField(blank=True, editable=False, null=True)),
                ('crr', models.FloatField(blank=True, editable=False, null=True)),
                ('fs', models.FloatField(blank=True, editable=False, null=True)),
                ('liquefaction_potential', models.CharField(blank=True, editable=False, max_length=10, null=True)),
                ('fl', models.FloatField(blank=True, editable=False, null=True)),
                ('f_z', models.FloatField(blank=True, editable=False, null=True)),
                ('fl_fz', models.FloatField(blank=True, editable=False, null=True)),
            ],
        ),
    ]
