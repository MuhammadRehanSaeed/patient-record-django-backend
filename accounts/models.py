from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Patient(models.Model):
    # Basic Information
    patient_name = models.CharField(max_length=255)
    mr_no = models.CharField(max_length=100, unique=True)  # Medical Record Number
    age = models.CharField(max_length=10)
    weight = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    
    # Dates
    admission_date = models.CharField(max_length=50)
    operation_date = models.CharField(max_length=50)
    discharge_date = models.CharField(max_length=50)
    
    # Medical Information
    comorbid = models.TextField()  # Comorbidities
    presenting_complain = models.TextField()
    examination = models.TextField()
    hand_written_diagnosis = models.TextField()
    classification = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    
    # Surgical Information
    procedure = models.TextField()
    operative = models.CharField(max_length=100)
    surgeon_name = models.CharField(max_length=255)
    pre_op_neurology = models.TextField()
    surgery = models.CharField(max_length=100)
    side = models.CharField(max_length=50)
    spine_level = models.CharField(max_length=100)
    
    # MRI and Imaging
    mri_findings = models.TextField()
    instrumentation = models.TextField()
    mri = models.CharField(max_length=100)
    
    # Post-operative
    after_complication = models.TextField()
    re_do_surgery = models.CharField(max_length=100)
    
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


