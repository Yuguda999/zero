# Django API for Managing People

This Django API allows you to manage information about people with CRUD operations. You can add, retrieve, update, and delete person records using this API.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [1. Add a New Person](#1-add-a-new-person)
  - [2. Fetch Details of a Person](#2-fetch-details-of-a-person)
  - [3. Modify the Details of an Existing Person](#3-modify-the-details-of-an-existing-person)
  - [4. Remove a Person](#4-remove-a-person)
- [Known Limitations](#known-limitations)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed
- Django 3.x installed
- `virtualenv` for managing Python virtual environments (optional but recommended)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd person-api
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install project dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the database in settings.py. You can use SQLite for development:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
Apply migrations to create the database:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Usage
1. Add a New Person
Endpoint: POST /api/people/
To add a new person, send a POST request with the person's data in the request body. Replace <api_base_url> with the actual URL where the API is hosted.

Request:

http
Copy code
POST <api_base_url>/api/people/
Content-Type: application/json

{
    "name": "Mark Essien"
}
Response (201 Created):

json
Copy code
{
    "name": "Mark Essien"
}
2. Fetch Details of a Person
Endpoint: GET /api/people/{name}/
To fetch details of a person by name, send a GET request with the person's name in the URL. Replace <api_base_url> and {name} with the actual API URL and person's name.

Request:

http
Copy code
GET <api_base_url>/api/people/Mark%20Essien/
Response (200 OK):

json
Copy code
{
    "name": "Mark Essien"
}
3. Modify the Details of an Existing Person
Endpoint: PUT /api/people/{name}/ or PATCH /api/people/{name}/
To modify the details of an existing person, send a PUT or PATCH request with the updated data in the request body and the person's name in the URL. Replace <api_base_url>, {name}, and the request body with actual values.

Request (PUT):

http
Copy code
PUT <api_base_url>/api/people/Mark%20Essien/
Content-Type: application/json

{
    "name": "Updated Mark Essien"
}
Response (200 OK):

json
Copy code
{
    "name": "Updated Mark Essien"
}
4. Remove a Person
Endpoint: DELETE /api/people/{name}/
To remove a person by name, send a DELETE request with the person's name in the URL. Replace <api_base_url> and {name} with the actual API URL and person's name.

Request:

http
Copy code
DELETE <api_base_url>/api/people/Updated%20Mark%20Essien/
Response (204 No Content)

Known Limitations
The API assumes that the "name" field should only contain letters and spaces. Any other characters are not allowed.
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this API.
