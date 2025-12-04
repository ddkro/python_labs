import argparse

def cat_command(input_file, n):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if n:
                for i, line in enumerate(lines, 1):
                    print(f"{i}: {line.rstrip()}")
            else:
                print(''.join(lines), end='')
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")

def stats_command(input_file, top):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            text = f.read().lower()
            words = text.split()
            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
            
            sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
            for word, freq in sorted_words[:top]:
                print(f"{word}: {freq}")
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)

if __name__ == "__main__":
    main()
