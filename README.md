**Spotify Playlist Data Pipeline**
This project fetches featured playlists from Spotify, saves the data to HDFS, and uploads CSV files to AWS S3. This pipeline facilitates further data analysis and visualization using AWS QuickSight.

**Table of Contents**
Overview
Features
Prerequisites
Installation
Configuration
Usage
Data Visualization
Contributing
License

***Overview:***
This data pipeline automates the process of collecting Spotify playlist data, storing it in HDFS, and transferring it to AWS S3. This pipeline is useful for data engineers and analysts who want to analyze and visualize Spotify data.

***Features:***
Fetch featured playlists from Spotify based on genres
Save playlist data as CSV files in HDFS
Upload CSV files from HDFS to AWS S3
Seamless integration with AWS QuickSight for data visualization

***Prerequisites:***
Python 3.7 or higher
Spotipy
HDFS client
Boto3
AWS account with S3 and QuickSight access
Spotify Developer account

***Installation:***
Clone the repository: https://github.com/2100031416-Ashok-Kumar/Spotify-Playlist-Data-Pipeline.git
Install the required Python packages: pip install -r requirements.txt

***Configuration***
Set up your Spotify Developer account and obtain your client_id and client_secret.

Configure your AWS credentials and specify your S3 bucket name.

Update the placeholders in the script with your actual credentials: client_id = 'YOUR_SPOTIFY_CLIENT_ID'
client_secret = 'YOUR_SPOTIFY_CLIENT_SECRET'
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'
bucket_name = 'YOUR_S3_BUCKET_NAME'

Replace YOUR_HDFS_USER with your actual HDFS user in the script.

***Usage:***
Run the script to fetch playlist data, save it to HDFS, and upload it to S3: python spotify_playlist_pipeline.py

The script will fetch playlists for the specified genres, save the data to HDFS as CSV files, download them locally, and upload them to the specified S3 bucket.

***Data Visualization:***
Sign in to AWS QuickSight.

Create a new data source and connect it to your S3 bucket.

Use the CSV files uploaded to S3 for your analysis and visualization.

***Contributing:***
Contributions are welcome! Please feel free to submit a Pull Request.

***License:***
This project is licensed under the MIT License. See the LICENSE file for details.
