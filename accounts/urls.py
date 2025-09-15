from django.urls import path
from .views import (
    LogoutView, RegisterView, LoginView,
    PatientCreateView, PatientListView, PatientDetailView, PatientSearchView, TestAuthView
)

urlpatterns = [
    # Authentication URLs
    path('signup/', RegisterView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    
    # Patient URLs
    path('patients/', PatientCreateView.as_view(), name="patient-create"),
    path('patients/list/', PatientListView.as_view(), name="patient-list"),
    path('patients/<int:patient_id>/', PatientDetailView.as_view(), name="patient-detail"),
    path('patients/search/', PatientSearchView.as_view(), name="patient-search"),
    
    # Test URL
    path('test-auth/', TestAuthView.as_view(), name="test-auth"),
]
