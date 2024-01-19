import re

def word_frequency(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()
            words = re.findall(r'\b\w+\b', text)
            word_freq = {word: words.count(word) for word in set(words)}
            sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            for word, count in sorted_word_freq:
                print(str(word) + ': ' + str(count))
    except FileNotFoundError:
        print(f"File {filename} not found.")

filename = "sample.txt" # replace with your own file name
word_frequency(filename)