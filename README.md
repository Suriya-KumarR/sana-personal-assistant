# AI Assistant with Dialogflow and FastAPI

This project demonstrates how to create an AI assistant using Dialogflow and a FastAPI backend. The assistant captures intents from Dialogflow and interacts with the various API's (such as Spotify and OpenWeather) to fulfil its tasks.

![image](https://github.com/suriyakumar99/sana-personal-assistant/assets/68340831/bfc27486-90f7-41d1-8fab-bc9a8659d9ab)

## Project Structure

- **Dialogflow Agent**: Located in `main/NewAgent`
- **FastAPI Backend**: Located in `main/fastapi_backend`

## Prerequisites

- [Python 3.7+](https://www.python.org/downloads/)
- [Dialogflow Account](https://dialogflow.cloud.google.com/)
- [Spotify Developer Account](https://developer.spotify.com/)
- [ngrok](https://ngrok.com/) (for local development)

## Setup

### Dialogflow Agent

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name/main/NewAgent
    ```

2. **Import Dialogflow Agent**:
    - Go to the [Dialogflow Console](https://dialogflow.cloud.google.com/).
    - Select your project or create a new one.
    - Click on the settings icon ⚙️ next to your agent's name.
    - Select the `Export and Import` tab.
    - Click `Restore from zip` and upload the `NewAgent` folder.

### FastAPI Backend

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name/main/fastapi_backend
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    Create a `.env` file in the `fastapi_backend` directory with your Spotify API credentials:
    ```env
    SPOTIFY_CLIENT_ID=your_spotify_client_id
    SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
    SPOTIFY_REFRESH_TOKEN=your_spotify_refresh_token
    ```

4. **Run the FastAPI Server**:
    ```bash
    uvicorn main:app --reload
    ```

5. **Expose Local Server** (for Dialogflow webhook):
    ```bash
    ngrok http 8000
    ```
    Copy the `https` URL provided by ngrok. This will be used as the webhook URL in Dialogflow.

### Dialogflow Webhook Integration

1. **Enable Webhook in Dialogflow**:
    - Go to the Dialogflow Console and select your agent.
    - Navigate to `Fulfillment` in the left menu.
    - Enable the `Webhook` option.
    - Set the `Webhook URL` to the ngrok `https` URL followed by `/webhook`. Example: `https://your-ngrok-url/webhook`.

2. **Use Webhook in Intents**:
    - Go to the `Intents` section.
    - Select the `welcome-morning` intent.
    - Scroll down to the `Fulfillment` section and enable `Webhook call for this intent`.

## Testing

1. **Interact with Your Agent**:
    - Use the Dialogflow Console to test your agent by typing "hey, morning".
    - The agent should respond with "Good morning Su! Tasks first or the news first?" and invoke the webhook.

2. **Check the FastAPI Logs**:
    - Ensure the FastAPI server logs show the webhook request and response handling.

## Additional Notes

- **Spotify API Authentication**: Ensure your Spotify API credentials are valid and have the necessary scopes.
- **Security**: Use HTTPS for all communications in production.
- **Error Handling**: Implement error handling in FastAPI to manage issues with API requests and webhook processing.

## License

This project is licensed under the MIT License.
