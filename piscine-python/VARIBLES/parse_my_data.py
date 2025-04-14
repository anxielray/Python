user_sentence = input("Please enter a sentence: ")
word_count = len(user_sentence.split())

lowercase_sentence = user_sentence.lower()

print(f"Number of words: {word_count}")
print(f"Lowercase sentence: {lowercase_sentence}")
print("Note: This is an example of preprocessing text data.")