import init
import whisper
from openai import OpenAI
from rich import print
import argparse
import gpt_translator
import copy
import ctx
from whisper.utils import get_writer


def panic(err_msg):
    print(f"[PANIC]: {err_msg}")
    while True:
        pass


def gpt_batch_translate(result):
    client = OpenAI()
    cloned_result = copy.deepcopy(result)
    for segment in result['segments']:
        print(f"text: {segment['text']}")
        text = segment['text']
        id = segment['id']

        answer = gpt_translator.translate(client,
                                          text,
                                          ctx.pred_text(result, id),
                                          ctx.succ_text(result, id))
        print(f"answer: {answer}\n")
        cloned_result['segments'][id]['text'] = answer
    return cloned_result


def main(video_file):
    init.init_env()
    model = whisper.load_model("large")
    result = model.transcribe(video_file)
    print(result)

    translate_result = gpt_batch_translate(result)
    writer = get_writer("srt", ".")  # get srt writer for the current directory
    output_file = video_file.replace(".mp4", "")
    writer(translate_result, f'{output_file}.srt', {})  # add empty dictionary for 'options'


if __name__ == '__main__':
    print("Hello, this is VidTrans.")
    parser = argparse.ArgumentParser(description="VidTrans: Video Transcription Tool")
    parser.add_argument('--file', type=str, help='Path to the video file to be transcribed')

    args = parser.parse_args()
    main(args.file)
