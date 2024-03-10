import moviepy.editor as mp
import imageio
import os
import math

def split_video_to_gifs(input_video, output_folder, gif_fps=30,clip_duration=5):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Load the video clip
    video_clip = mp.VideoFileClip(input_video)

    # Get the duration of the video in seconds
    duration = int(video_clip.duration)

    # Split the video into 1-second-long clips
    for i in range(0, duration, clip_duration):
        start_time = i
        end_time = min(i + clip_duration, duration)

        # Create a subclip from the original video
        subclip = video_clip.subclip(start_time, end_time)

        # Get the frames as a list
        frames = [frame for frame in subclip.iter_frames(fps=gif_fps)]

        # Save the frames as a GIF in the output folder
        gif_filename = os.path.join(output_folder, f"{math.ceil(i/clip_duration)}.gif")
        imageio.mimsave(gif_filename, frames, fps=gif_fps)

    # Close the video clip
    video_clip.reader.close()

if __name__ == "__main__":
    input_video_path = 'badapple-square.mp4'
    output_folder_path = 'clip'
    gif_framerate = 30
    clip_duration = 15

    split_video_to_gifs(input_video_path, output_folder_path, gif_fps=gif_framerate,clip_duration=clip_duration)
