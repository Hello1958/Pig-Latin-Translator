# Pig Latin Translator
This is a Pig Latin translator. This repository contains various modules concerned with encoding and decoding Pig Latin. (Sidenote: the decode function uses AI for translation, and you will need a Google AI API key in order to use it.) See the license (MIT License) and Code of Conduct for appropriate usage guidlines.

## API Key
To get started with decoding, navigate to the decode module (aptly named decode.py). From lines 1 through 11 there will be instructions on how to get your API key. Once you have the key, there are multiple ways to get started.

### Method 1: Environment Variable
Method 1 uses environment variables and the os module to access Google AI. This method avoids hardcoding your API key into the code, so it is probably the best option in terms of security. (Note that you may have to restart your session in order for the variable to take effect.) In order to set this environment variable, navigate to the terminal and type this command: setx API_KEY "your API key" Paste your API key where it says "your API key". Do not remove the quotation marks. Then, press enter and the variable should be set.

### Method 2: Hardcoding the Variable
This method is arguably easier but probably less secure compared to method 1. In decode.py, go to line 20 and replace "os.environ["API_KEY"]" with your API key. Remember to put your key in as a string; that is, surrounded by quotes. Then, you can remove line 14 and line 18.

## Running the Translator
Navigate to the file named Pig Latin Translator.py and run it. Now, you should be good to go!
