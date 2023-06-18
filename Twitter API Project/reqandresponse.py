import openai
import tweepy
import random
import logging
from typing import List

openai.api_key = "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"


def generate_chat_response(messages: list) -> str:
    """Takes a list of dictionaries and returns a string message
    Generates a chatGPT response from the API, note: Requires credit on openai website
    If any exceptions are caught, log the error and return None
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0,
        )

        chat_response = response["choices"][0]["message"]["content"]
        return chat_response

    except openai.OpenAIError as e:
        logging.error("OpenAI API Error: %s", str(e))
        return None

    except requests.exceptions.RequestException as e:
        logging.error("Request Exception: %s", str(e))
        return None


def extract_questions(filename: str) -> list:
    """Takes a filename as input and generates a list of questions in the format below

    messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is HTML?"},
    ]
    """

    questions = []

    with open(filename, "r") as q_file:
        # creating an iterable list of strings, with each element being a message
        text_list: list = (q_file.read()).split("\n")

        for question in text_list:
            msg_dict = {"role": "user", "content": question}
            questions.append(msg_dict)

    return questions


def tweet(tweet: str):
    """Takes a string as input and tweets that string"""
    consumer_key = "K3GHMEkGoYJQQaywJsvouYN2S"
    consumer_secret = "2RHnRIP3SdJoZedvPfRYOfeih4fL8C3eCFgGn02bKU7b7H1XxL"

    access_token = "1668830207552409603-vfSXOOdTX69XI8MF0e0grQvWaFERvm"
    access_token_secret = "ciKmz2d0W6poM9ShqnQ6vgEHfCXvLmdFYs471IRA3IWIp"

    client = tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )
    # The app and the corresponding credentials must have the Write permission
    # Check the App permissions section of the Settings tab of your app, under the
    # Twitter Developer Portal Projects & Apps page at
    # https://developer.twitter.com/en/portal/projects-and-apps

    # Make sure to reauthorize your app / regenerate your access token and secret
    # after setting the Write permission

    response = client.create_tweet(text=tweet)
    print(f"https://twitter.com/user/status/{response.data['id']}")


def main():
    # Generates a list of questions in the correct format
    # One question at a time
    # questions_list = extract_questions("my_questions.txt")

    # for question in questions_list:
    #     response = generate_chat_response(question)
    #     if response == None:
    #         print("There is an error with the response")
    #     else:
    #         tweet(question)

    response = generate_chat_response(
        [
            {
                "role": "system",
                "content": "You are a helpful assistant",
            },
            {
                "role": "user",
                "content": "Give me 10 questions related to the attack of Pearl Harbor seperated by \n",
            },
        ]
    )


if __name__ == "__main__":
    main()
# generate chat response takes as input a list of dictionaries in the above format
