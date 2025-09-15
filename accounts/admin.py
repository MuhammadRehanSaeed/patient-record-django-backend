from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [
        'patient_name', 'mr_no', 'age', 'gender', 'city', 
        'phone_no', 'admission_date', 'created_at', 'created_by'
    ]
    list_filter = [
        'gender', 'city', 'created_at', 'created_by'
    ]
    search_fields = [
        'patient_name', 'mr_no', 'phone_no', 'city'
    ]
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('patient_name', 'mr_no', 'age', 'weight', 'height', 'gender', 'city', 'phone_no')
        }),
        ('Dates', {
            'fields': ('admission_date', 'operation_date', 'discharge_date')
        }),
        ('Medical Information', {
            'fields': ('comorbid', 'presenting_complain', 'examination', 'hand_written_diagnosis', 'classification', 'value')
        }),
        ('Surgical Information', {
            'fields': ('procedure', 'operative', 'surgeon_name', 'pre_op_neurology', 'surgery', 'side', 'spine_level')
        }),
        ('MRI and Imaging', {
            'fields': ('mri_findings', 'instrumentation', 'mri')
        }),
        ('Post-operative', {
            'fields': ('after_complication', 're_do_surgery')
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
