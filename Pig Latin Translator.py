"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python

Get your Google AI API key here:
https://aistudio.google.com/app/apikey
Use your Google account to sign in for the key. (It's free ;) )
"""

from encode_sentence import encode_sentence
from decode import decode, ai_setup

API_KEY = ""

if __name__ == "__main__":
    ai_setup(API_KEY)
    while True:
        dENcoder: str = input('Would you like to encode or decode Pig Latin?\nEnter 1 to encode\nEnter 2 to decode\n')
        if dENcoder == '1':
            print("\n", encode_sentence(input('> ')))
        elif dENcoder == '2':
            print("\n", decode(input('> ')))
        else:
            print("Please enter a valid choice.")
            continue
