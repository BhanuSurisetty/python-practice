# Word Frequency Counter

def word_frequency_counter(text):
    freq= {}
    words = text.split()
    for word in words:
        word = word.lower()
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq

if __name__ == "__main__":
    text = input("enter a text: ")
    frequency = word_frequency_counter(text)
    print("Word Frequency:")
    for word, count in frequency.items():
        print(f"{word}: {count}")
