from encode_special_characters import encode_special_characters
VOWELS: list[str] = ["a", "e", "i", "o", "u"]
DIGITS: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
SPECIAL_CHARACTERS: list[str] = ['/', ';', "'", '[', ']', '\\', '`', '-', '=', '<', '>', ':', '"', '{', '}', '|', '~', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
PUNCTUATION: list[str] = [",", ".", "?", "!"]


def plaintext_last_step_conversion(ciphertext, encrypted_letter="y"):
    ciphertext.append(f"{encrypted_letter}ay")
    ciphertext = ''.join([str(elem) for i, elem in enumerate(ciphertext)])
    return ciphertext


def encode_word(plaintext) -> str:
    if not list(plaintext):
        plaintext = list(plaintext)
        plaintext.append(" ")
        plaintext = ''.join(plaintext)
    weird_plaintext = list(plaintext)
    plaintext = plaintext.lower()
    plaintext_list = list(plaintext)
    
    if set(list(plaintext_list)) & set(PUNCTUATION) or set(list(plaintext)) & set(SPECIAL_CHARACTERS):
        ciphertext = encode_special_characters(plaintext)
        return ciphertext
    else:
        if set(list(plaintext)) & set(DIGITS):
            return plaintext
        elif len(plaintext) == 1:
            if plaintext in VOWELS:
                ciphertext = list(plaintext)
                ciphertext = plaintext_last_step_conversion(ciphertext)
                return ciphertext
            else:
                return plaintext
        elif weird_plaintext[0] in VOWELS:
            ciphertext = list(plaintext)
            ciphertext = plaintext_last_step_conversion(ciphertext)
            return ciphertext
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
            return ciphertext