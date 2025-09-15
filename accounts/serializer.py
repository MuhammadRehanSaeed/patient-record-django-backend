from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password
from .models import Patient


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'id', 'patient_name', 'mr_no', 'age', 'weight', 'height', 'gender', 
            'city', 'phone_no', 'admission_date', 'comorbid', 'presenting_complain', 
            'examination', 'hand_written_diagnosis', 'classification', 'value', 
            'operation_date', 'discharge_date', 'procedure', 'operative', 
            'surgeon_name', 'pre_op_neurology', 'surgery', 'side', 'spine_level', 
            'mri_findings', 'instrumentation', 'mri', 'after_complication', 
            're_do_surgery', 'created_at', 'updated_at', 'created_by'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'created_by']
    
    def create(self, validated_data):
        # Set the created_by field to the current user
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
