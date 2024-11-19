import cv2
import numpy as np

# Set video parameters
fps = 24
frame_size = (400, 400)
duration = 5  # seconds for the entire division process

# Calculate the total number of frames
total_frames = fps * duration

# Define the video writer
output_path = r"C:\Users\joel\Desktop\CS230\project\multi_cell_division_animation.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, frame_size, isColor=True)

# Animation parameters
radius = 15  # size of each cell
num_stages = 4
stage_duration = total_frames // num_stages  # frames per division stage

# Predefined positions for each stage
positions_by_stage = [
    [(200, 200)],  # Stage 1: 1 cell in the center
    [(150, 200), (250, 200)],  # Stage 2: 2 cells on left and right
    [(150, 150), (250, 150), (150, 250), (250, 250)],  # Stage 3: 4 cells in a square
    [(100, 100), (300, 100), (100, 300), (300, 300),
     (100, 200), (200, 100), (200, 300), (300, 200)],  # Stage 4: 8 cells
]

# Mapping of parent cells to daughter cells for each division
mappings = [
    # Stage 1 to Stage 2
    [(0, [0, 1])],
    # Stage 2 to Stage 3
    [(0, [0, 2]), (1, [1, 3])],
    # Stage 3 to Stage 4
    [(0, [0, 4]), (1, [1, 5]), (2, [2, 6]), (3, [3, 7])],

]

# Start with the first stage
current_positions = positions_by_stage[0]

# Generate frames for each division stage
for stage in range(1, len(positions_by_stage)):
    target_positions = positions_by_stage[stage]
    mapping = mappings[stage - 1]

    # Prepare a list to store the movement of daughter cells
    position_data = []
    for parent_index, daughter_indices in mapping:
        x_p, y_p = current_positions[parent_index]
        for daughter_index in daughter_indices:
            x_d, y_d = target_positions[daughter_index]
            # The daughter cell starts at the parent's position
            x_i, y_i = x_p, y_p
            position_data.append((daughter_index, x_i, y_i, x_d, y_d))

    # Sort position_data by daughter indices
    position_data.sort(key=lambda x: x[0])

    # Generate frames for the division
    for frame_num in range(stage_duration):
        frame = np.ones((frame_size[1], frame_size[0], 3), dtype=np.uint8) * 255
        progress = frame_num / stage_duration  # Transition progress

        interpolated_positions = []
        for idx, x_i, y_i, x_d, y_d in position_data:
            x = int(x_i * (1 - progress) + x_d * progress)
            y = int(y_i * (1 - progress) + y_d * progress)
            interpolated_positions.append((x, y))

        # Draw cells at interpolated positions
        for pos in interpolated_positions:
            cv2.circle(frame, pos, radius, (0, 0, 0), -1)

        # Write the frame to the video
        out.write(frame)

    # Update current_positions for the next stage
    current_positions = target_positions.copy()

# Release the video writer
out.release()
print(f"Video saved as {output_path}")
