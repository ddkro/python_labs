from text import *

def main():

    input_text = input()

    normalized = normalize(input_text)

    tokens = tokenize(normalized)

    freq = count_freq(tokens)

    top5 = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top5:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()
