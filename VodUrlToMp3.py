import requests
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from moviepy.editor import VideoFileClip

# URL of the video you want to download
video_url = "https://sjcu4.ktcdn.co.kr/lec/_definst_/502287/502287-01.mp4"

# Extract the filename from the URL
video_filename = os.path.basename(video_url)
print(video_filename)
audio_filename =os.path.splitext(video_filename)[0] + ".mp3"

base_path ="D:/deeplearning/sjcu_working/20232/Resource/"
# Specify file paths for the downloaded video and converted audio
video_path = base_path + video_filename
audio_path = base_path + "/audio/" + audio_filename


try:
    # Send an HTTP GET request to the URL
    response = requests.get(video_url, stream=True)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        with open(video_path, 'wb') as file:
            # Iterate over the content of the response in chunks and save it to a file
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print("Video downloaded successfully and saved as:", video_path)

        # Convert the downloaded video to MP3
        video_clip = VideoFileClip(video_path)
        video_clip.audio.write_audiofile(audio_path, codec='mp3')
        print("Video converted to MP3 and saved as:", audio_path)
    else:
        print("Failed to download the video. Status code:", response.status_code)
except Exception as e:
    print("An error occurred:", str(e))
