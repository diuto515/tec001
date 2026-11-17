import string


def word_frequency(text):
    frequency = {}
    for word in text.lower().split():
        word = word.strip(string.punctuation)
        if word:
            frequency[word] = frequency.get(word, 0) + 1
    return frequency


def main():
    text = input("Enter a piece of text: ")
    frequency = word_frequency(text)
    for word, count in frequency.items():
        print(f"{word}: {count}")


main()