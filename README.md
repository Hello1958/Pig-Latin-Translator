# Pig Latin Translator
This is a Pig Latin translator. This repository contains various modules concerned with encoding and decoding Pig Latin. (Sidenote: the decode function uses AI for translation, and you will need a Google AI API key in order to use it.) See the license (MIT License) and Code of Conduct for appropriate usage guidlines.

## API Key
To get started with decoding, navigate to the decode module (aptly named decode.py). From lines 1 through 11 there will be instructions on how to get your API key. Once you have the key, there are multiple ways to get started.
![Screenshot 2024-07-13 131041](https://github.com/user-attachments/assets/90a9daf0-b77c-4c98-9cae-0620442afc6e)

### Method 1: Environment Variable
Method 1 uses environment variables and the os module to access Google AI. This method avoids hardcoding your API key into the code, so it is probably the best option in terms of security. (Note that you may have to restart your session in order for the variable to take effect.) In order to set this environment variable, navigate to the terminal and type this command: setx API_KEY "your API key" Paste your API key where it says "your API key". Do not remove the quotation marks. Then, press enter and the variable should be set. If this doesn't work and you get an error, try method 2.
![Screenshot 2024-07-13 132052](https://github.com/user-attachments/assets/385dc907-4133-49a2-829f-dd84b1857c96)


### Method 2: Hardcoding the Variable
This method is arguably easier but probably less secure compared to method 1. In decode.py, go to line 20 and replace "os.environ["API_KEY"]" with your API key. Remember to put your key in as a string; that is, surrounded by quotes. Then, you can remove line 14 and line 18.
![Screenshot 2024-07-13 132313](https://github.com/user-attachments/assets/d0183731-5c5b-4b9e-ac7c-5d46b83f11ff)

## Running the Translator
Navigate to the file named Pig Latin Translator.py and run it. Now, you should be good to go!
