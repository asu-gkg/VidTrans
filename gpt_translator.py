from rich import print

domain = 'Advanced Network System'
src = 'English'
dst = 'Chinese'


def translate(client, english_text, pred, succ):
    prompt = (f"You are an expert in {domain}. Your task is to translate a lecture from {src} to {dst}. "
              f"I will provide the sentence to be translated along with its preceding and succeeding context. "
              f"Translate only the provided sentence from {src} into {dst}. "
              f"Preceding context: {pred}. "
              f"Succeeding context: {succ}. "
              f"Sentence to translate: {english_text}.")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": english_text
            }
        ],
        temperature=0.7,
        max_tokens=64,
        top_p=1
    )
    return response.choices[0].message.content
