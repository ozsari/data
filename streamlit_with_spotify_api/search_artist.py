import requests

def search_artist(token, artist_name):
    """
    Search for an artist on Spotify using the provided token and artist name.

    Args:
    token (str): The OAuth token used for authorization.
    artist_name (str): The name of the artist to search for.

    Returns:
    dict: A dictionary containing information about the artist.

    Raises:
    Exception: If the request to the Spotify API fails.
    """
    
    # Set up the authorization header with the provided token
    headers = {
        'Authorization': f'Bearer {token}'
    }
    
    # Set up the query parameters for the search request
    params = {
        'q': artist_name,
        'type': 'artist',
        'limit': 1  # Limit the search results to one artist
    }
    
    # Make a GET request to the Spotify API's search endpoint
    response = requests.get(
        'https://api.spotify.com/v1/search', headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Return the first artist found in the search results
        return response.json()['artists']['items'][0]
