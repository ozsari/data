import requests

def get_artist_albums(token, artist_id):
    """
    Retrieve the albums of an artist from Spotify using the provided token and artist ID.

    Args:
    token (str): The OAuth token used for authorization.
    artist_id (str): The Spotify ID of the artist whose albums are to be retrieved.

    Returns:
    list: A list of dictionaries, each containing information about an album.

    Raises:
    Exception: If the request to the Spotify API fails.
    """
    
    # Set up the authorization header with the provided token
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    # Set up the query parameters to include only albums and limit the results to 10
    params = {
        'include_groups': 'album',
        'limit': 10  # Limit the number of albums returned to 10
    }
    
    # Make a GET request to the Spotify API's artist albums endpoint
    response = requests.get(
        f'https://api.spotify.com/v1/artists/{artist_id}/albums', headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the list of albums found in the response
        return response.json
