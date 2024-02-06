import requests

def obtain_api_token(username, password, auth_url):
    # Prepare the authentication payload
    auth_payload = {
        'username': username,
        'password': password,
        # Add any additional parameters required for authentication
    }

    # Send a POST request to obtain the API token
    response = requests.post(auth_url, data=auth_payload)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the token from the response
        token = response.json().get('access_token')
        return token
    else:
        # Print an error message if authentication fails
        print(f"Authentication failed. Status code: {response.status_code}")
        return None

def make_authenticated_request(api_url, token):
    # Prepare headers with the obtained token for authentication
    headers = {
        'Authorization': f'Bearer {token}',
        # Add any other required headers
    }

    # Make an authenticated GET request to the API
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        print("Authenticated request successful.")
        print("Response:", response.json())
    else:
        print(f"Authenticated request failed. Status code: {response.status_code}")

if __name__ == "__main__":
    # Replace these values with your actual credentials and URLs
    username = 'your_username'
    password = 'your_password'
    auth_url = 'https://example.com/authenticate'  # Replace with your authentication endpoint
    api_url = 'https://example.com/api/resource'  # Replace with your API endpoint

    # Obtain the API token
    token = obtain_api_token(username, password, auth_url)

    # Make an authenticated request using the obtained token
    if token:
        make_authenticated_request(api_url, token)
