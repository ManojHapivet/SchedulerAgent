"""
Configuration file for Hospital Scheduling System
Store test credentials and API endpoints
"""

import os

# Production credentials - Use environment variables in production
PRODUCTION_CREDENTIALS = {
    "email": "sailokesh7780@gmail.com",
    "password": os.environ.get("PRODUCTION_PASSWORD", "Password@123"),
    "tenant_domain": None,
    "location_id": None
}

# Production tenant configuration - Happy Paws Veterinary Clinic
PRODUCTION_TENANT = {
    "tenant_id": "a9872e13-f580-400d-ad81-489a92f4ca56",
    "tenant_name": "Happy Paws Veterinary Clinic new",
    "location_id": "1b86f045-a2c3-43f2-adbf-6e60703ad352", 
    "location_name": "Happy Paws Main Branch"
}

# API Endpoints (Azure Functions compatible)
API_ENDPOINTS = {
    "auth_base_url": os.environ.get("AUTH_BASE_URL", "https://dev-hv-auth.azurewebsites.net"),
    "scheduler_base_url": os.environ.get("SCHEDULER_BASE_URL", "https://dev-hapivet-sch.azurewebsites.net")
}

# Test credentials for local development/demo purposes
TEST_CREDENTIALS = {
    "email": os.environ.get("TEST_EMAIL", "santosh@ibolinva.com"),
    "password": os.environ.get("TEST_PASSWORD", "Password@123"),
    "tenant_domain": os.environ.get("TEST_TENANT_DOMAIN"),
    "location_id": os.environ.get("TEST_LOCATION_ID")
}

# Hospital API Endpoints (adjust these based on actual API documentation)
HOSPITAL_API_ENDPOINTS = {
    "operating_hours": "/api/v1/HospitalOperatingHours/location",
    "break_timings": "/api/v1/BreakTimings/location",
    "holidays": "/api/v1/Holidays/location", 
    "overtime": "/api/v1/Overtime/location",
    "staff_schedule": "/api/v1/StaffSchedule/location",
    "appointments": "/api/v1/Appointments/location"
}

# OpenAI API Configuration (Azure Functions compatible)
OPENAI_CONFIG = {
    "model": "gpt-4o-mini",
    "temperature": 0.1,
    "api_key": os.environ.get("OPENAI_API_KEY", "your-openai-api-key-here")
}

# Request timeout settings
REQUEST_TIMEOUT = 30

# Logging configuration
LOGGING_LEVEL = "INFO"
