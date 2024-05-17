domain = 'Advanced Network System'
src = 'English'
dst = 'Chinese'


def translate(client, english_text, pred, succ):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"You are a expert in {domain}. Now you are trying to translate a lecture from {src} to"
                           f"{dst}. Your task is translate the sentence I give you from {src} into {dst}."
                           "To let you know the context of the text, I will give you the pred context and succ "
                           "context. Please only transfer the English sentence the user give you. You don't have to " + pred +
                           f"give other response. Notice the previous context is {pred}. And succ context is {succ}."},
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
