import sys                                  

from text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv

def main():
    
    input_path = 'data/input.txt'            
    output_path = 'data/report.csv'        
    encoding = 'utf-8'                      

   
    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv):
            if arg == '--in' and i+1 < len(sys.argv):
                input_path = sys.argv[i+1]
            if arg == '--out' and i+1 < len(sys.argv):
                output_path = sys.argv[i+1]
            if arg == '--encoding' and i+1 < len(sys.argv):
                encoding = sys.argv[i+1]


    try:
        text = read_text(input_path, encoding=encoding)
    except FileNotFoundError:
        print(f"Ошибка: файл '{input_path}' не найден.")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка кодировки для файла '{input_path}'. Попробуйте другое значение --encoding.")
        sys.exit(1)

    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    header = ('word', 'count')
    write_csv(sorted_items, output_path, header=header)


    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, 5):
        print(f"{word}:{count}")

if __name__ == '__main__':
    main()
