!pip install yt-dlp moviepy

import os
from yt_dlp import YoutubeDL

def download_and_convert_to_mp3(video_url, output_mp3_path):
    # Temporary file for downloaded audio
    temp_audio_file = "temp_audio.mp3"

    # Download the audio from YouTube using yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',  # Only download audio
        'outtmpl': temp_audio_file,  # Save directly to mp3
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Convert to mp3
            'preferredquality': '192',  # Quality setting
        }],
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print("Audio downloaded and converted successfully.")

        # The output file is already in MP3 format (temp_audio.mp3), so no further conversion needed
        print(f"MP3 saved at: {temp_audio_file}")

    except Exception as e:
        print("An error occurred:", e)

# Usage
video_url = "https://youtu.be/sYpSpHq9ziM?feature=shared"  # Replace with actual YouTube URL
output_mp3_path = "C:\\Users\HP\\Downloads\\MP33"

download_and_convert_to_mp3(video_url, output_mp3_path)

from google.colab import files

file_name = "temp_audio.mp3.mp3"
files.download(file_name)
