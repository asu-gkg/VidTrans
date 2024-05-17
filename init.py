import os
from huggingface_hub import login

OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'
HUGGING_FACE_LOGIN_TOKEN = 'YOUR_HUGGING_FACE_LOGIN_TOKEN'


def init_env():
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
    login(token=HUGGING_FACE_LOGIN_TOKEN)
