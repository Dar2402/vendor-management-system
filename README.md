# Vendor Management System with Performance Metrics

This is a Vendor Management System developed using Django and Django REST Framework. The system handles vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Database Setup

- Configure your database settings in `settings.py`.
- Run migrations to create database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Superuser (Optional)

To access the Django admin panel, you can create a superuser:

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

### 6. Access the API Endpoints

- Once the development server is running, you can access the API endpoints using the provided URLs:

    - Vendor Profile Management: `http://localhost:8000/api/vendors/`
    - Purchase Order Tracking: `http://localhost:8000/api/purchase_orders/`
    - Vendor Performance Evaluation: `http://localhost:8000/api/vendors/{vendor_id}/performance`

### 7. Generate Fake Data (Optional)

You can use management commands or scripts to generate fake data for testing purposes:

```bash
python manage.py generate_fake_data
```

### 8. Token-Based Authentication

- API endpoints are secured with token-based authentication. Obtain a token by sending a POST request to `http://localhost:8000/api/token/`.
