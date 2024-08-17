To test the API endpoints using Postman, follow these steps for each endpoint:

### 1. User Registration

**Endpoint:** `POST /api/register/`

**Request Body:**
```json
{
    "username": "testuser",
    "email": "testuser@example.com",
    "phone_number": "1234567890",
    "address": "123 Main St",
    "pin_code": "123456",
    "city": "Test City",
    "country": "Test Country",
    "password": "yourpassword"
}
```

**Steps:**
- Open Postman.
- Select **POST** from the dropdown.
- Enter the URL (e.g., `http://localhost:8000/api/register/`).
- Go to the **Body** tab, select **raw**, and choose **JSON** from the dropdown.
- Paste the JSON request body.
- Click **Send**.

### 2. User Login

**Endpoint:** `POST /api/login/`

**Request Body:**
```json
{
    "username": "testuser",
    "password": "yourpassword"
}
```

**Steps:**
- Select **POST** from the dropdown.
- Enter the URL (e.g., `http://localhost:8000/api/login/`).
- Go to the **Body** tab, select **raw**, and choose **JSON** from the dropdown.
- Paste the JSON request body.
- Click **Send**.

### 3. Forgot Password

**Endpoint:** `POST /api/forgot-password/`

**Request Body:**
```json
{
    "email": "testuser@example.com"
}
```

**Steps:**
- Select **POST** from the dropdown.
- Enter the URL (e.g., `http://localhost:8000/api/forgot-password/`).
- Go to the **Body** tab, select **raw**, and choose **JSON** from the dropdown.
- Paste the JSON request body.
- Click **Send**.

### 4. Create Incident

**Endpoint:** `POST /api/incidents/`

**Request Body:**
```json
{
    "details": "Incident description here",
    "priority": "High",
    "status": "Open"
}
```

**Headers:**
- Add `Authorization` header with the value `Basic <base64_encoded(username:password)>` or use token-based authentication if implemented.

**Steps:**
- Select **POST** from the dropdown.
- Enter the URL (e.g., `http://localhost:8000/api/incidents/`).
- Go to the **Body** tab, select **raw**, and choose **JSON** from the dropdown.
- Paste the JSON request body.
- Click **Send**.

### 5. View Incidents

**Endpoint:** `GET /api/incidents/`

**Headers:**
- Same as above for authentication.

**Steps:**
- Select **GET** from the dropdown.
- Enter the URL (e.g., `http://localhost:8000/api/incidents/`).
- Click **Send**.

### 6. Edit Incident

**Endpoint:** `PUT /api/incidents/<id>/`

**Request Body:**
```json
{
    "details": "Updated incident description",
    "priority": "Medium",
    "status": "In Progress"
}
```

**Headers:**
- Same as above for authentication.

**Steps:**
- Select **PUT** from the dropdown.
- Enter the URL (e.g., `http://localhost:8000/api/incidents/1/`).
- Go to the **Body** tab, select **raw**, and choose **JSON** from the dropdown.
- Paste the JSON request body.
- Click **Send**.

### 7. Search Incident by ID

**Endpoint:** `GET /api/incidents/search/<incident_id>/`

**Steps:**
- Select **GET** from the dropdown.
- Enter the URL (e.g., `http://localhost:8000/api/incidents/search/RMG123452022/`).
- Click **Send**.

### Notes

- Ensure your Django server is running (e.g., `python manage.py runserver`).
- Replace `localhost:8000` with your server's address if it's hosted elsewhere.
- If using token-based authentication, make sure to include the token in the headers.
- Check the response status and body in Postman to verify that the API is working as expected.

You can also check the **Console** in Postman for any errors or additional information.