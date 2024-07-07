from encode_word import encode_word


def encode_sentence(plaintext):
    plaintexts: list[str] = plaintext.split(" ")
    ciphertext: list[str] = []
    for plaintext1 in plaintexts:
        encrypted_plaintext = encode_word(plaintext1)
        ciphertext.append(encrypted_plaintext)
    ciphertext = ' '.join([str(elem) for i, elem in enumerate(ciphertext)])
    return ciphertext