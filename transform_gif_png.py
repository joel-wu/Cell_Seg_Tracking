import cv2
from PIL import Image
import numpy as np
import os

# Open the GIF file
gif_path = r"C:\Users\joel\Desktop\CS230\project\Substack (1-39)bt_close.gif"
gif = Image.open(gif_path)

output_folder = r"C:\Users\joel\Desktop\CS230\project\output_frames"  # Folder to save PNG frames

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open the GIF
gif = Image.open(gif_path)

# Extract each frame, ignoring the last one
frame_index = 0
while True:
    try:
        # Set the GIF to the current frame
        gif.seek(frame_index)

        # Convert the frame to grayscale (if not already) and save as JPG
        frame = gif.convert('L')  # 'L' mode for grayscale

        # Define the output path for the current frame
        frame_output_path = os.path.join(output_folder, f'frame_{frame_index}.jpg')

        # Save the frame as a JPG
        frame.save(frame_output_path, format="JPEG", quality=95)  # Save with high quality

        frame_index += 1
    except EOFError:
        # Exit loop when no more frames
        break

print(f"Frames saved in folder: {output_folder}")