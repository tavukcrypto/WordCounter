def count_words(sentence):
    words = sentence.split()
    return len(words)

def main():
    sentence = input("Enter a sentence: ")
    word_count = count_words(sentence)
    print(f"The sentence '{sentence}' contains {word_count} words.")

if __name__ == "__main__":
    main()
