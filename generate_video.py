import cv2
import os
import glob

# Set the path to the folder containing the images and the output video path
image_folder = r"C:\Users\joel\Desktop\CS230\project\Fluo-N2DL-HeLa\02"
output_path = r"C:\Users\joel\Desktop\CS230\project\Fluo-N2DL-HeLa\video_02.mp4"

# Define frames per second for the video
fps = 12

# Retrieve all .tif files in the specified folder, sorted by name
image_files = sorted(glob.glob(os.path.join(image_folder, "*.tif")))

# Read the first image to get the frame size
first_image = cv2.imread(image_files[0], cv2.IMREAD_GRAYSCALE)
height, width = first_image.shape

# Define the video codec and create a VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 format
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), isColor=False)

# Loop through each image file and write it to the video
for filename in image_files:
    # Read the image in grayscale
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    # Write the frame to the video
    out.write(img)

# Release the VideoWriter object
out.release()
print(f"Video created successfully at '{output_path}'")