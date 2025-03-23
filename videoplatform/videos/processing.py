import dataclasses
import pathlib

import cv2
from moviepy import VideoFileClip


@dataclasses.dataclass
class VideoDetails:
    duration: float
    size: list
    framerate: float = None


def get_video_metadata(path):
    video = VideoFileClip(path)
    details = VideoDetails(video.duration, video.size)
    details.framerate = video.fps
    return dataclasses.asdict(details)


def get_video_frames(path, k=2):
    if isinstance(path, str):
        path = pathlib.Path(path)

    if not path.is_file() and not path.exists():
        raise ValueError('Video is not valid')

    count = 0
    capture = cv2.VideoCapture(path)

    while capture.isOpened():
        if count > k:
            break

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        success, frame = capture.read()

        if not success:
            continue

        cv2.imwrite(f"frame{count}.jpg", frame)
        count = count + 1
