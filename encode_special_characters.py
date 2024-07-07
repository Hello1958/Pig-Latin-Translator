import re

VOWELS: list[str] = ["a", "e", "i", "o", "u"]
DIGITS: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SPECIAL_CHARACTERS: list[str] = ['/', ';', "'", '[', ']', '\\', '`', '-', '=', '<', '>', ':', '"', '{', '}', '|', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
PUNCTUATION: list[str] = [",", ".", "?", "!"]


def plaintext_last_step_conversion(ciphertext, encrypted_letter="y"):
    ciphertext.append(f"{encrypted_letter}ay")
    ciphertext = ''.join([str(elem) for i, elem in enumerate(ciphertext)])
    return ciphertext


def encode_spec_char(plaintext, punctuation):
    weird_plaintext = list(plaintext)
    if not list(plaintext):
        plaintext = list(plaintext)
        plaintext.append(" ")
        plaintext = ''.join(plaintext)
    if set(plaintext) & set(DIGITS):
            return plaintext
    elif len(plaintext) == 1:
            return plaintext
    elif set(weird_plaintext[0]) & set(VOWELS):
        ciphertext = list(plaintext)
        ciphertext = plaintext_last_step_conversion(ciphertext)
        ciphertext = list(ciphertext)
        ciphertext.append(punctuation)
        ciphertext = ''.join([str(elem) for i, elem in enumerate(ciphertext)])
        return "".join(ciphertext) 
    else:
        letter_selected_index = 0
        letter_selected = list(plaintext)[0]
        consonants: list[str] = []
        while letter_selected not in VOWELS:
            consonants.append(letter_selected)
            letter_selected_index += 1
            try:
                letter_selected = list(plaintext)[letter_selected_index]
            except IndexError:
                break
        ciphertext = list(plaintext)
        encrypted_letter = ''.join([str(elem) for i, elem in enumerate(consonants)])
        ciphertext = ''.join([str(elem) for i, elem in enumerate(ciphertext)])
        ciphertext = ciphertext[letter_selected_index:]
        ciphertext = list(ciphertext)
        ciphertext = plaintext_last_step_conversion(ciphertext=ciphertext, encrypted_letter=encrypted_letter)
        ciphertext = list(ciphertext)
        ciphertext.append(punctuation)
        ciphertext = ''.join([str(elem) for i, elem in enumerate(ciphertext)])
        return ciphertext


def encode_special_characters(plaintext):
    if set(list(plaintext)) & set(SPECIAL_CHARACTERS):
        return plaintext
    else:
        punctuation_places = []
        for i, char in enumerate(plaintext):
            if char in PUNCTUATION:
                punctuation_places.append(char) 

        split_words = re.split(f"[{re.escape(''.join(PUNCTUATION))}]+",plaintext)
        
        complete_string: list[str] = []
        punctuation_places += [''] * (len(split_words) - len(punctuation_places))  # Add empty strings for padding
        for index, word in enumerate(split_words):
            complete_string.append(encode_spec_char(word, punctuation_places[int(index)]))

        complete_string = ''.join([str(elem) for i, elem in enumerate(complete_string)])
        return complete_string 
