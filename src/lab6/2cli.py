import argparse
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.lab5.json_csv import json_to_csv, csv_to_json
from src.lab5.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    # json2csv
    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    # csv2json
    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    # csv2xlsx
    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    try:
        if args.cmd == "json2csv":
            if not os.path.exists(args.input):
                raise FileNotFoundError(f"Входной файл не найден: {args.input}")
            json_to_csv(args.input, args.output)
            print(f"Конвертировано: {args.input} → {args.output}")
            
        elif args.cmd == "csv2json":
            if not os.path.exists(args.input):
                raise FileNotFoundError(f"Входной файл не найден: {args.input}")
            csv_to_json(args.input, args.output)
            print(f"Конвертировано: {args.input} → {args.output}")
            
        elif args.cmd == "csv2xlsx":
            if not os.path.exists(args.input):
                raise FileNotFoundError(f"Входной файл не найден: {args.input}")
            csv_to_xlsx(args.input, args.output)
            print(f"Конвертировано: {args.input} → {args.output}")
            
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        return 1
    except Exception as e:
        parser.error(f"Ошибка конвертации: {str(e)}")
        return 1

if __name__ == "__main__":
    exit(main() or 0)
