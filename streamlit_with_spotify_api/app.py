import streamlit as st
from datetime import datetime
from spotify_auth import get_access_token
from search_artist import search_artist
from get_albums import get_artist_albums
from get_related_artists import get_related_artists
from dotenv import load_dotenv
import os


load_dotenv()

st.title('Spotify Search Albums By Artist')

# Spotify API info
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

if client_id and client_secret:
    try:
        token = get_access_token(client_id, client_secret)
        # st.success('Access token successfully generated!')
    except Exception as e:
        st.error(f"Failed to get access token: {e}")

# Search artist
artist_name = st.text_input(
    'Search Albums By Artist Name', help='Enter artist name and press Enter.')

if artist_name and token:
    try:
        artist = search_artist(token, artist_name)

        # Placing artist information into two columns
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(artist['images'][0]['url'], width=200)

        with col2:
            st.subheader(artist['name'].title())
            st.markdown(
                f"[Spotify Link]({artist['external_urls']['spotify']})")
            followers_formatted = "{:,}".format(artist['followers']['total'])
            st.write(f"Followers: {followers_formatted.replace(',', '.')}")
            st.write(f"Genres: {', '.join(artist['genres']).title()}")

        st.write("")  # empty line added
        st.write("")

        albums = get_artist_albums(token, artist['id'])
        st.subheader('Albums')

        # Album cover handling
        num_columns = 5
        cols = st.columns(num_columns)

        for i, album in enumerate(albums):
            with cols[i % num_columns]:
                st.markdown(
                    f"""
                    <div style="display: flex; flex-direction: column; align-items: center; height: 250px; margin-bottom: 20px;">
                        <img src="{album['images'][0]['url']}" style="width: 100%; height: auto;"/>
                        <a href="{album['external_urls']['spotify']}" style="text-align: center; margin-top: 10px; text-decoration:none;">{album['name'] + " (" + str(datetime.strptime(album['release_date'], '%Y-%m-%d').year) + ")"}</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.write("")
        st.subheader('Similar Artists')

        related_artists = get_related_artists(token, artist['id'])

        cols = st.columns(5)
        # Top 10 similar artists
        for i, related_artist in enumerate(related_artists[:10]):
            with cols[i % 5]:
                st.markdown(
                    f"""
                    <div style="display: flex; flex-direction: column; align-items: center; height: auto; margin-bottom: 20px;">
                        <img src="{related_artist['images'][0]['url']}" style="width: 100px; height: 100px; border-radius: 50%;"/>
                        <a href="{related_artist['external_urls']['spotify']}" style="text-align: center; margin-top: 10px; text-decoration:none">{related_artist['name']}</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    except Exception as e:
        st.error(f"Artist not found: {e}")
