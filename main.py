import re

def count_words(text):
    words = re.split(r'[ ,:;]+', text)
    words = list(filter(lambda x: x.strip(), words))
    return len(words)


def count_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    sentences = list(filter(lambda x: x.strip(), sentences))
    return len(sentences)


def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()


def write_result_to_file(filepath, words, sentences):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(f'Words: {words}\n')
        file.write(f'Sentences: {sentences}')


if __name__ == "__main__":
    filepath = input("Введіть шлях до файлу: ")
    text = read_file(filepath)
    words = count_words(text)
    sentences = count_sentences(text)
    write_result_to_file('result.txt', words, sentences)
