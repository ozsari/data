import requests


def get_related_artists(token, artist_id):
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(
        f'https://api.spotify.com/v1/artists/{artist_id}/related-artists', headers=headers)

    if response.status_code == 200:
        return response.json()['artists']
    else:
        raise Exception(f"Failed to get related artists: {
                        response.status_code}")
