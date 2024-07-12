import requests
import base64

# To use the Spotify API, we first need to generate a token.

def get_access_token(client_id, client_secret):
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    auth_headers = {
        'Authorization': f'Basic {b64_auth_str}'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(
        'https://accounts.spotify.com/api/token', headers=auth_headers, data=auth_data)

    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception(f"Failed to get access token: {response.status_code}")
