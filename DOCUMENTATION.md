# API Documentation

## Standard Formats for Requests and Responses

### Person Data Format (JSON)

```json
{
    "name": "Mark Essien",
    // Add other fields as needed
}
Endpoints
1. Add a New Person
Endpoint: POST /api/people/
Request Format:
Method: POST
Headers: Content-Type: application/json
Body: Person Data (JSON)
Response Format:
Status Code: 201 (Created)
Body: Newly created person data (JSON)
2. Fetch Details of a Person
Endpoint: GET /api/people/{name}/
Request Format:
Method: GET
Response Format:
Status Code: 200 (OK)
Body: Person data (JSON)
3. Modify the Details of an Existing Person
Endpoint: PUT /api/people/{name}/ or PATCH /api/people/{name}/
Request Format:
Method: PUT or PATCH
Headers: Content-Type: application/json
Body: Updated person data (JSON)
Response Format:
Status Code: 200 (OK)
Body: Updated person data (JSON)
4. Remove a Person
Endpoint: DELETE /api/people/{name}/
Request Format:
Method: DELETE
Response Format:
Status Code: 204 (No Content)
Sample Usage
1. Add a New Person
Request:

http
Copy code
POST /api/people/
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
Request:

http
Copy code
GET /api/people/Mark%20Essien/
Response (200 OK):

json
Copy code
{
    "name": "Mark Essien"
}
3. Modify the Details of an Existing Person
Request:

http
Copy code
PUT /api/people/Mark%20Essien/
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
Request:

http
Copy code
DELETE /api/people/Updated%20Mark%20Essien/
Response (204 No Content)

Known Limitations and Assumptions
The API assumes that the "name" field should only contain letters and spaces. Any other characters are not allowed.
Setup and Deployment
To set up and deploy the API locally or on a server, follow these steps:

Clone the project repository:

bash
Copy code
git clone <repository_url>
Install Python and Django (if not already installed).

Create a virtual environment and activate it:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install project dependencies:

bash
Copy code
pip install -r requirements.txt
Configure the database in settings.py.

Apply migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
The API will be accessible at http://localhost:8000/api/.

For deployment on a server, configure a production-ready web server (e.g., Gunicorn) and set up a database server (e.g., PostgreSQL).

Update the API's base URL in your client scripts to match the server's URL.

Ensure proper security measures for the production environment, including HTTPS, authentication, and authorization.

Please replace <repository_url> with the actual URL of your project's Git repository
