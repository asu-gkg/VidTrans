# VidTrans

VidTrans is an innovative framework designed to enhance the translation
of academic videos using a combination of large language models (LLMs) and Whisper.

# Installation

## Set up a virtual environment

``` 
python3 -m venv vid_trans
source vid_trans/bin/activate
pip install -r requirements.txt
```

## Set up your api keys

``` 
touch init.py
```

Change `OPENAI_API_KEY` and `HUGGING_FACE_LOGIN_TOKEN` in `init.py` file.

# Usage

Test with `example.mp4`

``` 
make run
```

Translate your videos file:

``` 
make run FILE=YOUR_OWN_FILE
```
