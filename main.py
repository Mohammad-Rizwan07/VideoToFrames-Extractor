import cv2
import os

# Use your actual full video path here:
video_path = r"sample_video/my_video.mp4"  # <-- Change this!

output_folder = 'video_frames'
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ ERROR: Could not open video. Check the path or file format.")
    exit()

frame_count = 0
success, frame = cap.read()

while success:
    filename = os.path.join(output_folder, f"frame_{frame_count:05d}.jpg")
    cv2.imwrite(filename, frame)
    frame_count += 1
    success, frame = cap.read()

cap.release()
print(f"✅ Done! Extracted {frame_count} frames to folder: {output_folder}")
