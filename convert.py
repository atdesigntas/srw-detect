import os
import cv2
import argparse

def convert_avi_to_mp4(input_path, output_path):
    """Convert an AVI video file to MP4 format using OpenCV."""
    cap = cv2.VideoCapture(input_path)
    
    # Get the video's properties (frame width, height, and FPS)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create a VideoWriter object for MP4 output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Read and write each frame to the new video file
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
    
    # Release resources
    cap.release()
    out.release()
    print(f"Video saved as {output_path}")

def main():

    parser = argparse.ArgumentParser(description='Verify Yolo Annotations')
    parser.add_argument('--input_path', type=str, help='Path to video file')
    parser.add_argument('--save_path', type=str, help='Path to save video file')
    args = parser.parse_args()

    args = parser.parse_args()

    #os.makedirs(args.save_path, exist_ok=True)

    convert_avi_to_mp4(args.input_path, args.save_path)

if __name__ == '__main__':
	main()
