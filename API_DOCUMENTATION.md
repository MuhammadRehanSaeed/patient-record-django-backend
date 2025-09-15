# Patient Record API Documentation

## Base URL
```
http://127.0.0.1:8000/api/
```

## Authentication
All patient endpoints require JWT authentication. Include the access token in the Authorization header:
```
Authorization: Bearer <your_access_token>
```

## Endpoints

### 1. Create Patient Record
**POST** `/api/patients/`

Creates a new patient record.

**Request Body:**
```json
{
    "patient_name": "John Doe",
    "mr_no": "MR001",
    "age": "45",
    "weight": "70",
    "height": "175",
    "gender": "Male",
    "city": "New York",
    "phone_no": "+1234567890",
    "admission_date": "2024-01-15",
    "comorbid": "Diabetes, Hypertension",
    "presenting_complain": "Lower back pain",
    "examination": "Lumbar spine examination",
    "hand_written_diagnosis": "Lumbar disc herniation",
    "classification": "Type A",
    "value": "High",
    "operation_date": "2024-01-20",
    "discharge_date": "2024-01-25",
    "procedure": "Lumbar discectomy",
    "operative": "Yes",
    "surgeon_name": "Dr. Smith",
    "pre_op_neurology": "Normal",
    "surgery": "Lumbar",
    "side": "Left",
    "spine_level": "L4-L5",
    "mri_findings": "Disc herniation at L4-L5",
    "instrumentation": "Pedicle screws",
    "mri": "Yes",
    "after_complication": "None",
    "re_do_surgery": "No"
}
```

**Response (201 Created):**
```json
{
    "message": "Patient record created successfully",
    "patient": {
        "id": 1,
        "patient_name": "John Doe",
        "mr_no": "MR001",
        "age": "45",
        "weight": "70",
        "height": "175",
        "gender": "Male",
        "city": "New York",
        "phone_no": "+1234567890",
        "admission_date": "2024-01-15",
        "comorbid": "Diabetes, Hypertension",
        "presenting_complain": "Lower back pain",
        "examination": "Lumbar spine examination",
        "hand_written_diagnosis": "Lumbar disc herniation",
        "classification": "Type A",
        "value": "High",
        "operation_date": "2024-01-20",
        "discharge_date": "2024-01-25",
        "procedure": "Lumbar discectomy",
        "operative": "Yes",
        "surgeon_name": "Dr. Smith",
        "pre_op_neurology": "Normal",
        "surgery": "Lumbar",
        "side": "Left",
        "spine_level": "L4-L5",
        "mri_findings": "Disc herniation at L4-L5",
        "instrumentation": "Pedicle screws",
        "mri": "Yes",
        "after_complication": "None",
        "re_do_surgery": "No",
        "created_at": "2024-01-15T10:30:00Z",
        "updated_at": "2024-01-15T10:30:00Z",
        "created_by": 1
    }
}
```

### 2. Get All Patients
**GET** `/api/patients/list/`

Retrieves all patient records for the authenticated user.

**Response (200 OK):**
```json
{
    "message": "Patients retrieved successfully",
    "patients": [
        {
            "id": 1,
            "patient_name": "John Doe",
            "mr_no": "MR001",
            // ... all patient fields
        }
    ],
    "count": 1
}
```

### 3. Get Patient by ID
**GET** `/api/patients/{patient_id}/`

Retrieves a specific patient record by ID.

**Response (200 OK):**
```json
{
    "message": "Patient retrieved successfully",
    "patient": {
        "id": 1,
        "patient_name": "John Doe",
        // ... all patient fields
    }
}
```

### 4. Update Patient (Full Update)
**PUT** `/api/patients/{patient_id}/`

Updates a patient record with all fields.

**Request Body:** Same as create patient
**Response (200 OK):** Same as create patient

### 5. Update Patient (Partial Update)
**PATCH** `/api/patients/{patient_id}/`

Updates specific fields of a patient record.

**Request Body:**
```json
{
    "patient_name": "John Smith",
    "phone_no": "+1234567891"
}
```

**Response (200 OK):** Updated patient data

### 6. Delete Patient
**DELETE** `/api/patients/{patient_id}/`

Deletes a patient record.

**Response (204 No Content):**
```json
{
    "message": "Patient record deleted successfully"
}
```

### 7. Search Patients
**GET** `/api/patients/search/?search=query`

Searches patients by name, MR number, or phone number.

**Query Parameters:**
- `search`: Search term (required)

**Example:** `/api/patients/search/?search=John`

**Response (200 OK):**
```json
{
    "message": "Search results for 'John'",
    "patients": [
        {
            "id": 1,
            "patient_name": "John Doe",
            // ... all patient fields
        }
    ],
    "count": 1
}
```

## Error Responses

### 400 Bad Request
```json
{
    "message": "Validation error",
    "errors": {
        "field_name": ["Error message"]
    }
}
```

### 401 Unauthorized
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### 404 Not Found
```json
{
    "message": "Patient not found",
    "error": "Error details"
}
```

## Testing with cURL

### 1. Create a patient:
```bash
curl -X POST http://127.0.0.1:8000/api/patients/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "patient_name": "John Doe",
    "mr_no": "MR001",
    "age": "45",
    "weight": "70",
    "height": "175",
    "gender": "Male",
    "city": "New York",
    "phone_no": "+1234567890",
    "admission_date": "2024-01-15",
    "comorbid": "Diabetes, Hypertension",
    "presenting_complain": "Lower back pain",
    "examination": "Lumbar spine examination",
    "hand_written_diagnosis": "Lumbar disc herniation",
    "classification": "Type A",
    "value": "High",
    "operation_date": "2024-01-20",
    "discharge_date": "2024-01-25",
    "procedure": "Lumbar discectomy",
    "operative": "Yes",
    "surgeon_name": "Dr. Smith",
    "pre_op_neurology": "Normal",
    "surgery": "Lumbar",
    "side": "Left",
    "spine_level": "L4-L5",
    "mri_findings": "Disc herniation at L4-L5",
    "instrumentation": "Pedicle screws",
    "mri": "Yes",
    "after_complication": "None",
    "re_do_surgery": "No"
  }'
```

### 2. Get all patients:
```bash
curl -X GET http://127.0.0.1:8000/api/patients/list/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 3. Search patients:
```bash
curl -X GET "http://127.0.0.1:8000/api/patients/search/?search=John" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Notes

1. All string fields accept any string value as per your Flutter model requirements
2. The `mr_no` field must be unique across all patients
3. All endpoints require authentication except for login/signup
4. Users can only access their own patient records
5. The API returns consistent JSON responses with message and data fields
6. All timestamps are in ISO format
7. The `created_by` field is automatically set to the authenticated user

