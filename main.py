import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "./config/secret.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    request = youtube.playlistItems().list(
        part="id,contentDetails,snippet",
        playlistId="PLgUIFmZuDRxAjFaQm9jewXwyfBe23yVsD"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()