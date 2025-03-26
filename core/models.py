from django.db import models

class SoilData(models.Model):
    # User input fields
    depth = models.FloatField(help_text="Depth in meters")
    unit_weight = models.FloatField(help_text="Unit weight in kN/m3")
    measured = models.IntegerField(help_text="Measured (N) value")
    soil_type = models.CharField(
        max_length=1,
        choices=[('s', 'Sand/Nonplastic Silt'), ('c', 'Silt/Clay')],
        help_text="Soil Type"
    )
    uscs_classification = models.CharField(max_length=20, help_text="USCS Classification")
    fc = models.FloatField(help_text="Fine Content (FC%)")
    er = models.FloatField(help_text="Energy Ratio (ER%)")
    peak_ground_acceleration = models.FloatField(help_text="Peak Ground Acceleration (g)")
    earthquake_magnitude = models.FloatField(help_text="Earthquake Magnitude (M)")
    water_table_depth = models.FloatField(help_text="Water Table Depth (m)")
    borehole_diameter = models.FloatField(help_text="Borehole Diameter (mm)")
    requires_correction_sampler_liners = models.BooleanField(help_text="Requires Correction for Sampler Liners (Yes/No)")
    rod_length = models.FloatField(help_text="Rod Length (depth + 1.5m)")
    
    # Auto-calculated fields
    ce = models.FloatField(editable=False, null=True, blank=True)
    cb = models.FloatField(editable=False, null=True, blank=True)
    cr = models.FloatField(editable=False, null=True, blank=True)
    initial_cs = models.FloatField(editable=False, null=True, blank=True)
    mid_cs = models.FloatField(editable=False, null=True, blank=True)
    final_cs = models.FloatField(editable=False, null=True, blank=True)
    initial_n60 = models.FloatField(editable=False, null=True, blank=True)
    mid_n60 = models.FloatField(editable=False, null=True, blank=True)
    final_n60 = models.FloatField(editable=False, null=True, blank=True)
    incremental_total_stress = models.FloatField(editable=False, null=True, blank=True, help_text="Incremental total stress (kPa)")
    svc = models.FloatField(editable=False, null=True, blank=True, help_text="Total vertical stress (svc) (kPa)")
    svc_prime = models.FloatField(editable=False, null=True, blank=True, help_text="Effective vertical stress (s'vc) (kPa)")
    cn = models.FloatField(editable=False, null=True, blank=True)
    initial_n1_60 = models.FloatField(editable=False, null=True, blank=True)
    mid_n1_60 = models.FloatField(editable=False, null=True, blank=True)
    final_n1_60 = models.FloatField(editable=False, null=True, blank=True)
    dr = models.FloatField(editable=False, null=True, blank=True)
    adjusted_fc = models.FloatField(editable=False, null=True, blank=True)
    f = models.FloatField(editable=False, null=True, blank=True)
    v_s = models.FloatField(editable=False, null=True, blank=True)
    rd = models.FloatField(editable=False, null=True, blank=True)
    csr = models.FloatField(editable=False, null=True, blank=True)
    dwfm_sand = models.FloatField(editable=False, null=True, blank=True)
    ks = models.FloatField(editable=False, null=True, blank=True)
    crr = models.FloatField(editable=False, null=True, blank=True)
    fs = models.FloatField(editable=False, null=True, blank=True)
    liquefaction_potential = models.CharField(max_length=10, editable=False, null=True, blank=True)
    fl = models.FloatField(editable=False, null=True, blank=True)
    f_z = models.FloatField(editable=False, null=True, blank=True)
    fl_fz = models.FloatField(editable=False, null=True, blank=True)
    
    def calculate_cb(self):
        if self.borehole_diameter < 115.1:
            return 1
        elif self.borehole_diameter < 150.1:
            return 1.05
        else:
            return 1.15
    
    def calculate_initial_cs(self):
        value = 1 + self.measured / 100
        adjusted_value = max(1.1, value)
        return min(adjusted_value, 1.3)
    
    def calculate_cr(self):
        value = self.depth + 1.5
        if value < 3:
            return 0.75
        elif value < 4:
            return 0.8
        elif value < 6:
            return 0.85
        elif value < 10:
            return 0.95
        else:
            return 1
    
    def calculate_mid_cs(self):
        value = 1 + self.initial_n1_60 / 100
        adjusted_value = max(1.1, value)
        return min(adjusted_value, 1.3)
    
    def calculate_final_cs(self):
        value = 1 + self.mid_n1_60 / 100
        adjusted_value = max(1.1, value)
        return min(adjusted_value, 1.3)

    def calculate_initial_n60(self):
        return self.measured * self.ce * self.cb * self.cr * self.initial_cs
    
    def calculate_mid_n60(self):
        return self.measured * self.ce * self.cb * self.cr * self.mid_cs
    
    def calculate_final_n60(self):
        return self.measured * self.ce * self.cb * self.cr * self.final_cs
    
    def save(self, *args, **kwargs):
        self.ce = self.er/60
        self.cb = self.calculate_cb()
        self.cr = self.calculate_cr()
        self.initial_cs = self.calculate_initial_cs()
        self.mid_cs = self.calculate_mid_cs()
        self.final_cs = self.calculate_final_cs()
        self.initial_n60 = self.calculate_initial_n60()
        self.mid_n60 = self.calculate_mid_n60()
        self.final_n60 = self.calculate_final_n60()
        
        self.svc = self.depth * self.unit_weight
        self.svc_prime = self.svc - (self.fc * 0.1)
        self.incremental_total_stress = self.svc - self.svc_prime
        self.cn = 1.0 + (0.1 * self.depth)
        self.initial_n1_60 = self.initial_n60 * self.cn
        self.mid_n1_60 = self.mid_n60 * self.cn
        self.final_n1_60 = self.final_n60 * self.cn
        self.dr = (self.initial_n1_60 / 100) * 100
        self.adjusted_fc = self.fc * 0.95
        self.f = 1.0  # Placeholder formula
        self.v_s = 1.0  # Placeholder formula
        self.rd = 1.0  # Placeholder formula
        self.csr = self.svc / self.unit_weight  # Placeholder formula
        self.dwfm_sand = 1.0  # Placeholder formula
        self.ks = 1.0  # Placeholder formula
        self.crr = self.csr / 2  # Example placeholder
        self.fs = self.crr / self.csr  # Factor of Safety calculation
        self.liquefaction_potential = "Yes" if self.fs < 1 else "No"
        self.fl = 1.0  # Placeholder formula
        self.f_z = 1.0  # Placeholder formula
        self.fl_fz = self.fl * self.f_z  # Example calculation
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Soil Data at {self.depth}m - {self.uscs_classification}"


