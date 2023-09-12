# API Documentation

This document provides detailed information about the endpoints, request/response formats, and usage examples for the Django API used to manage people.

## Table of Contents

- [Endpoints](#endpoints)
  - [1. Add a New Person](#1-add-a-new-person)
  - [2. Fetch Details of a Person](#2-fetch-details-of-a-person)
  - [3. Modify the Details of an Existing Person](#3-modify-the-details-of-an-existing-person)
  - [4. Remove a Person](#4-remove-a-person)
- [Request and Response Formats](#request-and-response-formats)
  - [1. Add a New Person](#1-add-a-new-person)
  - [2. Fetch Details of a Person](#2-fetch-details-of-a-person)
  - [3. Modify the Details of an Existing Person](#3-modify-the-details-of-an-existing-person)
  - [4. Remove a Person](#4-remove-a-person)
- [Sample Usage](#sample-usage)
  - [1. Add a New Person](#1-add-a-new-person)
  - [2. Fetch Details of a Person](#2-fetch-details-of-a-person)
  - [3. Modify the Details of an Existing Person](#3-modify-the-details-of-an-existing-person)
  - [4. Remove a Person](#4-remove-a-person)

## Endpoints

### 1. Add a New Person

- **Endpoint:** `POST /api/`
- **Description:** This endpoint allows you to add a new person to the database.
- **Request Format:**
  ```json
  {
      "name": "Mark Essien"
  }
  ```
- **Response Format:**
  ```json
  {
      "name": "Mark Essien"
  }
  ```

### 2. Fetch Details of a Person

- **Endpoint:** `GET /api/{name}/`
- **Description:** This endpoint allows you to fetch details of a person by their name.
- **Response Format:**
  ```json
  {
      "name": "Mark Essien"
  }
  ```

### 3. Modify the Details of an Existing Person

- **Endpoint:** `PUT /api/{name}/` or `PATCH /api/{name}/`
- **Description:** This endpoint allows you to modify the details of an existing person by their name.
- **Request Format:**
  ```json
  {
      "name": "Updated Mark Essien"
  }
  ```
- **Response Format:**
  ```json
  {
      "name": "Updated Mark Essien"
  }
  ```

### 4. Remove a Person

- **Endpoint:** `DELETE /api/{name}/`
- **Description:** This endpoint allows you to remove a person by their name.
- **Response Format:** 204 No Content

## Request and Response Formats

Detailed request and response formats for each endpoint are provided in the "Endpoints" section above.

## Sample Usage

### 1. Add a New Person

**Request:**
```http
POST <api_base_url>/api/
Content-Type: application/json

{
    "name": "Mark Essien"
}
```

**Response (201 Created):**
```json
{
    "name": "Mark Essien"
}
```

### 2. Fetch Details of a Person

**Request:**
```http
GET <api_base_url>/api/Mark%20Essien/
```

**Response (200 OK):**
```json
{
    "name": "Mark Essien"
}
```

### 3. Modify the Details of an Existing Person

**Request (PUT):**
```http
PUT <api_base_url>/api/Mark%20Essien/
Content-Type: application/json

{
    "name": "Updated Mark Essien"
}
```

**Response (200 OK):**
```json
{
    "name": "Updated Mark Essien"
}
```

### 4. Remove a Person

**Request:**
```http
DELETE <api_base_url>/api/Updated%20Mark%20Essien/
```

**Response (204 No Content)**
