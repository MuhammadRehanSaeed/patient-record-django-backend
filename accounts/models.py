from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Patient(models.Model):
    # Required Basic Information
    patient_name = models.CharField(max_length=255)
    mr_no = models.CharField(max_length=100, unique=True)  # Medical Record Number
    age = models.CharField(max_length=10)
    weight = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    
    # Optional Basic Information
    city = models.CharField(max_length=100, blank=True, default='')
    phone_no = models.CharField(max_length=20, blank=True, default='')
    
    # Optional Dates
    admission_date = models.CharField(max_length=50, blank=True, default='')
    operation_date = models.CharField(max_length=50, blank=True, default='')
    discharge_date = models.CharField(max_length=50, blank=True, default='')
    
    # Optional Medical Information
    comorbid = models.TextField(blank=True, default='')  # Comorbidities
    presenting_complain = models.TextField(blank=True, default='')
    examination = models.TextField(blank=True, default='')
    hand_written_diagnosis = models.TextField(blank=True, default='')
    classification = models.CharField(max_length=100, blank=True, default='')
    value = models.CharField(max_length=100, blank=True, default='')
    
    # Optional Surgical Information
    procedure = models.TextField(blank=True, default='')
    operative = models.CharField(max_length=100, blank=True, default='')
    surgeon_name = models.CharField(max_length=255, blank=True, default='')
    pre_op_neurology = models.TextField(blank=True, default='')
    surgery = models.CharField(max_length=100, blank=True, default='')
    side = models.CharField(max_length=50, blank=True, default='')
    spine_level = models.CharField(max_length=100, blank=True, default='')
    
    # Optional MRI and Imaging
    mri_findings = models.TextField(blank=True, default='')
    instrumentation = models.TextField(blank=True, default='')
    mri = models.CharField(max_length=100, blank=True, default='')
    
    # Optional Post-operative
    after_complication = models.TextField(blank=True, default='')
    re_do_surgery = models.CharField(max_length=100, blank=True, default='')
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
    
    def __str__(self):
        return f"{self.patient_name} - {self.mr_no}"


