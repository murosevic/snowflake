# Imports
from __future__ import annotations
import openai
import creds
import view
from multiprocessing import *

# API Key
openai.api_key = creds.apikey


def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[' Human:', ' AI:']
        )

        choices: dict = response.get('choices')[0]
        text = choices.get('text')

    except Exception as e:
        print('ERROR:', e)

    return text


def update_list(message: str, pl: list[str]):
    pl.append(message)


def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f'\nHuman: {message}'
    update_list(p_message, pl)
    prompt: str = ''.join(pl)
    return prompt


def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt)

    if bot_response:
        update_list(bot_response, pl)
        pos: int = bot_response.find('\nAI: ')
        bot_response = bot_response[pos + 5:]
    else:
        bot_response = 'Something went wrong...'

    return bot_response


def main(user_input):
    prompt_list: list[str] = ['You are an assistant and will answer as snowflake',
                              '\nHuman: What time is it?',
                              '\nAI: I have no idea, I\'m a snowflake!']

    while True:
        if user_input == "Stop program":
            print("Snowflake: Sure")
            exit()

        response = get_bot_response(user_input, prompt_list)
        print(f'Bot: {response}')