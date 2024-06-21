import csv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from hdfs import InsecureClient
import boto3

# Spotify API credentials
client_id = 'YOUR_SPOTIFY_CLIENT_ID'
client_secret = 'YOUR_SPOTIFY_CLIENT_SECRET'

# AWS S3 credentials
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'
bucket_name = 'YOUR_S3_BUCKET_NAME'

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Function to get featured playlists by genre
def get_featured_playlists_by_genre(genre):
    try:
        playlists = sp.category_playlists(category_id=genre, country='US', limit=10)
        playlist_items = []

        for playlist in playlists['playlists']['items']:
            playlist_tracks = sp.playlist_tracks(playlist['id'], limit=10)  # Limit to 10 tracks per playlist
            playlist['tracks'] = [track['track'] for track in playlist_tracks['items']]
            playlist_items.append(playlist)

        return playlist_items
    except spotipy.SpotifyException as e:
        print(f"Error fetching playlists for '{genre}': {str(e)}")
        return []

# Function to save data to HDFS as CSV
def save_data_to_hdfs_as_csv(data, hdfs_file_path):
    client = InsecureClient('http://localhost:9870', user='YOUR_HDFS_USER')

    try:
        with client.write(hdfs_file_path, encoding='utf-8') as writer:
            csv_writer = csv.writer(writer)
            csv_writer.writerow(['Playlist Name', 'Playlist ID', 'Track Name', 'Artist'])
            for playlist in data:
                for track in playlist['tracks']:
                    csv_writer.writerow([playlist['name'], playlist['id'], track['name'], track['artists'][0]['name']])
        print(f"Successfully saved data to HDFS as CSV: {hdfs_file_path}")
    except Exception as e:
        print(f"Error saving data to HDFS as CSV: {str(e)}")

# Function to upload CSV to S3
def upload_csv_to_s3(local_csv_path, s3_file_path):
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    try:
        s3_client.upload_file(local_csv_path, bucket_name, s3_file_path)
        print(f"Successfully uploaded CSV file {local_csv_path} to S3 bucket {bucket_name} as {s3_file_path}")
    except Exception as e:
        print(f"Error uploading CSV file to AWS S3: {str(e)}")

# Function to download data from HDFS to a local file
def download_from_hdfs(hdfs_file_path, local_csv_path):
    client = InsecureClient('http://localhost:9870', user='YOUR_HDFS_USER')

    try:
        with client.read(hdfs_file_path, encoding='utf-8') as reader:
            with open(local_csv_path, 'w', encoding='utf-8') as f:
                f.write(reader.read())
        print(f"Successfully downloaded {hdfs_file_path} to {local_csv_path}")
    except Exception as e:
        print(f"Error downloading file from HDFS: {str(e)}")
        raise

# Placeholder function to get related genres (to be replaced with actual logic)
def get_related_genres(genre):
    related_genres = ['related_genre1', 'related_genre2', 'related_genre3']
    return related_genres

if __name__ == "__main__":
    genres = ['pop', 'hiphop', 'rock', 'jazz']

    for genre in genres:
        playlists = get_featured_playlists_by_genre(genre)
        
        print(f"Saving playlists in {genre} to HDFS:")
        hdfs_file_path = f"/user/YOUR_HDFS_USER/spotify_playlists_{genre}.csv"
        
        save_data_to_hdfs_as_csv(playlists, hdfs_file_path)
        
        print(f"Uploading {hdfs_file_path} to S3:")
        local_csv_path = f"./{genre}.csv"
        
        try:
            download_from_hdfs(hdfs_file_path, local_csv_path)
            upload_csv_to_s3(local_csv_path, f"spotify_playlists_{genre}.csv")
        except Exception as e:
            print(f"Error processing {genre}: {str(e)}")
            continue

    genre_to_explore = 'pop'
    related_genres = get_related_genres(genre_to_explore)
    print(f"Related genres to {genre_to_explore}: {related_genres}")
