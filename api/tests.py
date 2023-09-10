import requests

base_url = 'http://localhost:8000/api/people/'  # Update with your API URL


# Function to make a POST request to add a new person
def create_person(name):
    data = {'name': name}
    response = requests.post(base_url, json=data)
    return response


# Function to make a GET request to fetch details of a person by name
def get_person_details(name):
    response = requests.get(f'{base_url}{name}/')
    return response


# Function to make a PUT request to modify the details of an existing person
def update_person(name, new_name):
    data = {'name': new_name}
    response = requests.put(f'{base_url}{name}/', json=data)
    return response


# Function to make a DELETE request to remove a person by name
def delete_person(name):
    response = requests.delete(f'{base_url}{name}/')
    return response


if __name__ == "__main__":
    # Add a new person
    new_person_name = "Mark Essien"
    create_response = create_person(new_person_name)
    if create_response.status_code == 201:
        print(f"New person '{new_person_name}' added successfully.")
    else:
        print(f"Failed to add a new person. Status code: {create_response.status_code}")

    # Fetch details of the person
    get_response = get_person_details(new_person_name)
    if get_response.status_code == 200:
        person_data = get_response.json()
        print(f"Details of '{new_person_name}': {person_data}")
    else:
        print(f"Failed to fetch details of the person. Status code: {get_response.status_code}")

    # Modify the details of the person
    updated_person_name = "Updated Mark Essien"
    update_response = update_person(new_person_name, updated_person_name)
    if update_response.status_code == 200:
        print(f"Details of '{new_person_name}' updated to '{updated_person_name}' successfully.")
    else:
        print(f"Failed to update details of the person. Status code: {update_response.status_code}")

    # Remove the person
    delete_response = delete_person(updated_person_name)
    if delete_response.status_code == 204:
        print(f"Person '{updated_person_name}' removed successfully.")
    else:
        print(f"Failed to remove the person. Status code: {delete_response.status_code}")
