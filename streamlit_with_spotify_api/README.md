
# Spotify API

To use Spotify's API, you first need to create an app. Here's how:

1. Log in with your Spotify account at https://developer.spotify.com/.
2. Then go to https://developer.spotify.com/dashboard and create an app.

<img width="800" alt="Untitled" src="https://github.com/user-attachments/assets/a9e5c003-7d13-46cd-85db-f16f87262c50">

3. Fill in the required information such as App Name and App Description. You can choose any name you like. For the Redirect URL, you can use https://example.org/callback as shown in the example.

<img width="800" alt="Untitled (1)" src="https://github.com/user-attachments/assets/5a5e09cb-0b6f-46a9-9265-f8c024f555aa">

4. Once you complete these steps and click "Create App," you will be given a client ID and a client secret.

<img width="800" alt="Untitled (2)" src="https://github.com/user-attachments/assets/0817c8bf-9a09-46a7-816b-763568535bf1">


5. Paste these two pieces of information into the appropriate place in the .env file.
6. Create a virtual environment in Python: **python3.11 -m venv .venv**
7. Activate the virtual environment: **source .venv/bin/activate**
8. Install the required libraries: **pip install -r requirements.txt**
9. Finally, run **streamlit run app.py** to access the Streamlit dashboard.

## Demo


https://github.com/user-attachments/assets/a036c6b1-f72d-4586-9b9a-fe7b91f9f2db

