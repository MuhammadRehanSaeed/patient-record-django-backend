from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from .serializer import RegisterSerializer, PatientSerializer
from .models import Patient
from django.shortcuts import get_object_or_404
from django.db import models


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            return Response({
                "message": "Signup successful",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # ⛔ Add refresh token to blacklist
            return Response({"message": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"error": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)
        except TokenError:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)


# Patient API Views
class PatientCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Create a new patient record
        """
        serializer = PatientSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            patient = serializer.save()
            return Response({
                "message": "Patient record created successfully",
                "patient": PatientSerializer(patient).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Validation error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class PatientListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get all patient records for the authenticated user
        """
        patients = Patient.objects.filter(created_by=request.user)
        serializer = PatientSerializer(patients, many=True)
        return Response({
            "message": "Patients retrieved successfully",
            "patients": serializer.data,
            "count": patients.count()
        }, status=status.HTTP_200_OK)


class PatientDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        """
        Get a specific patient record by ID
        """
        try:
            patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
            serializer = PatientSerializer(patient)
            return Response({
                "message": "Patient retrieved successfully",
                "patient": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "message": "Patient not found",
                "error": str(e)
            }, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, patient_id):
        """
        Update a specific patient record by ID
        """
        try:
            patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
            serializer = PatientSerializer(patient, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Patient record updated successfully",
                    "patient": serializer.data
                }, status=status.HTTP_200_OK)
            return Response({
                "message": "Validation error",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message": "Patient not found",
                "error": str(e)
            }, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, patient_id):
        """
        Partially update a specific patient record by ID
        """
        try:
            patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
            serializer = PatientSerializer(patient, data=request.data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "message": "Patient record updated successfully",
                    "patient": serializer.data
                }, status=status.HTTP_200_OK)
            return Response({
                "message": "Validation error",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({
                "message": "Patient not found",
                "error": str(e)
            }, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, patient_id):
        """
        Delete a specific patient record by ID
        """
        try:
            patient = get_object_or_404(Patient, id=patient_id, created_by=request.user)
            patient.delete()
            return Response({
                "message": "Patient record deleted successfully"
            }, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({
                "message": "Patient not found",
                "error": str(e)
            }, status=status.HTTP_404_NOT_FOUND)


class PatientSearchView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Search patients by various fields
        Query parameters: search (searches in patient_name, mr_no, phone_no)
        """
        search_query = request.GET.get('search', '')
        if not search_query:
            return Response({
                "message": "Search query is required",
                "error": "Please provide a search parameter"
            }, status=status.HTTP_400_BAD_REQUEST)

        patients = Patient.objects.filter(
            created_by=request.user
        ).filter(
            models.Q(patient_name__icontains=search_query) |
            models.Q(mr_no__icontains=search_query) |
            models.Q(phone_no__icontains=search_query)
        )
        
        serializer = PatientSerializer(patients, many=True)
        return Response({
            "message": f"Search results for '{search_query}'",
            "patients": serializer.data,
            "count": patients.count()
        }, status=status.HTTP_200_OK)


class TestAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Test endpoint to verify authentication is working
        """
        return Response({
            "message": "Authentication successful!",
            "user": {
                "id": request.user.id,
                "username": request.user.username,
                "email": request.user.email
            },
            "headers_received": {
                "authorization": request.META.get('HTTP_AUTHORIZATION', 'Not provided'),
                "content_type": request.META.get('CONTENT_TYPE', 'Not provided')
            }
        }, status=status.HTTP_200_OK)
