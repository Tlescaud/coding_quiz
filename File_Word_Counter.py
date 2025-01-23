def count_words_in_file(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "File not found."

# Example usage

filename = 'File_Word_Counter.py'
word_count = count_words_in_file(filename)
print(f"The number of words in {filename} is {word_count}.")