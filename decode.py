import os

import google.generativeai as genai


def ai_setup(api_key):
  genai.configure(api_key=api_key)


# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)


def decode(ciphertext):
  response = chat_session.send_message(f"You are a Pig Latin translator. You have been tasked with translating this piece of text: '{ciphertext}' into readable English.")
  return response.text