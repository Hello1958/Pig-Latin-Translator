from encode_sentence import encode_sentence
from decode import decode

if __name__ == "__main__":
    while True:
        dENcoder: str = input('Would you like to encode or decode Pig Latin?\nEnter 1 To encode\nEnter 2 to decode\n')
        if dENcoder == '1':
            print("\n", encode_sentence(input('> ')))
        elif dENcoder == '2':
            print("\n", decode(input('> ')))
        else:
            print("Please enter a valid choice.")
            continue
