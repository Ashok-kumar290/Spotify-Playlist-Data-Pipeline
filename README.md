# Spotify Playlist Data Pipeline

This project fetches featured playlists from Spotify, saves the data to HDFS, and uploads CSV files to AWS S3. This pipeline facilitates further data analysis and visualization using AWS QuickSight.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Data Visualization](#data-visualization)
- [Contributing](#contributing)
- [License](#license)

## Overview

This data pipeline automates the process of collecting Spotify playlist data, storing it in HDFS, and transferring it to AWS S3. This pipeline is useful for data engineers and analysts who want to analyze and visualize Spotify data.

## Features

- Fetch featured playlists from Spotify based on genres
- Save playlist data as CSV files in HDFS
- Upload CSV files from HDFS to AWS S3
- Seamless integration with AWS QuickSight for data visualization

## Prerequisites

- Python 3.7 or higher
- Spotipy
- HDFS client
- Boto3
- AWS account with S3 and QuickSight access
- Spotify Developer account

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/2100031416-Ashok-Kumar/Spotify-Playlist-Data-Pipeline.git
   cd spotify-playlist-data-pipeline
