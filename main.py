import init
import whisper
from openai import OpenAI
from rich import print
import argparse


def panic(err_msg):
    print(f"[PANIC]: {err_msg}")
    while True:
        pass


def main(video_file):
    client = OpenAI()

    init.init_env()
    model = whisper.load_model("large")
    result = model.transcribe("example.mp4")
    print(result)


if __name__ == '__main__':
    print("Hello, this is VidTrans.")
    parser = argparse.ArgumentParser(description="VidTrans: Video Transcription Tool")
    parser.add_argument('--file', type=str, help='Path to the video file to be transcribed')

    # Parse arguments
    args = parser.parse_args()
    main(args.file)
