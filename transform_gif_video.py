import cv2
from PIL import Image
import numpy as np

# Open the GIF file
gif_path = r"C:\Users\joel\Desktop\CS230\project\Substack (1-39)bt_close.gif"
gif = Image.open(gif_path)

# Extract each frame, ignoring the last one
frames = []
frame_index = 0
while True:
    try:
        # Set the GIF to the current frame
        gif.seek(frame_index)

        # Convert the frame to grayscale (if not already) and to numpy array
        frame = gif.convert('L')  # 'L' mode for grayscale
        frame_np = np.array(frame)

        # Append the frame to the list
        frames.append(frame_np)
        frame_index += 1
    except EOFError:
        # Exit loop when no more frames
        break

# Remove the last frame
frames = frames[:-1]

# Set output video parameters
fps = 24  # Set the desired frame rate
output_path = 'output.mp4'
height, width = frames[0].shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), isColor=False)

# Define how many times to repeat each frame to match the desired total duration
# Assuming each original GIF frame should be displayed for around 0.5 seconds
repeat_count = fps // 8 # Repeat each frame enough to last for about 0.5 seconds

# Write each frame to the output video with duplicates to adjust playback speed
for frame in frames:
    for _ in range(repeat_count):
        out.write(frame)  # Write the same frame multiple times

# Release the video writer
out.release()
print(f"Video saved as {output_path}")
