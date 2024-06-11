from fastapi import FastAPI, Request
import requests
import json

app = FastAPI()

SPOTIFY_CLIENT_ID = "your_spotify_client_id"
SPOTIFY_CLIENT_SECRET = "your_spotify_client_secret"
SPOTIFY_REFRESH_TOKEN = "your_spotify_refresh_token"

def get_spotify_access_token():
    url = "https://accounts.spotify.com/api/token"
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": SPOTIFY_REFRESH_TOKEN,
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    access_token = response.json().get("access_token")
    return access_token

def get_liked_songs(access_token):
    url = "https://api.spotify.com/v1/me/tracks"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    songs = response.json().get("items", [])
    liked_songs = [song['track']['name'] for song in songs]
    return liked_songs

@app.post("/webhook")
async def dialogflow_webhook(request: Request):
    body = await request.json()
    
    # Extract the intent name from the request
    intent_name = body['queryResult']['intent']['displayName']

    # Check if the intent is the "welcome-morning" intent
    if intent_name == "welcome-morning":
        access_token = get_spotify_access_token()
        liked_songs = get_liked_songs(access_token)

        # Prepare the response to be sent back to Dialogflow
        fulfillment_text = f"Here are your liked songs on Spotify: {', '.join(liked_songs)}"
        response = {
            "fulfillmentText": fulfillment_text
        }

        return response

    return {"fulfillmentText": "Intent not recognized."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
