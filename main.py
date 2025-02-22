import gdown
import os
import subprocess

# Step 1: Download video from Google Drive
file_id = "14eTVcP0noBz31TCYNVpoA54bLKGBs9Cs"  # Google Drive file ID
output = "video.mp4"

print("📥 Downloading video from Google Drive...")
gdown.download(f"https://drive.google.com/uc?export=download&id={file_id}", output, quiet=False)

# Step 2: Stream the downloaded video to YouTube Live
stream_key = "YOUR_STREAM_KEY"  # 🔴 Apni YouTube Stream Key yahan dalna!

print("🚀 Starting Live Stream...")

ffmpeg_command = f"""
ffmpeg -re -i {output} \
-c:v libx264 -preset veryfast -b:v 2500k \
-c:a aac -b:a 128k -ar 44100 \
-f flv "rtmp://a.rtmp.youtube.com/live2/{stream_key}"
"""

# Run FFmpeg
subprocess.run(ffmpeg_command, shell=True)
