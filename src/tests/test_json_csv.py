import json, csv
from pathlib import Path
import pytest 
import sys
sys.path.append(r'C:\Users\User\Desktop\python_labs\src')
from lab5.json_csv import json_to_csv, csv_to_json


def write_json(path: Path, obj): 
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path): 
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_json_to_csv_roundtrip(tmp_path: Path):
    '''тест конвертации из JSON в CSV'''
    src = tmp_path / "people.json" 
    dst = tmp_path / "people.csv"  
    data = [ 
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    write_json(src, data) 
    json_to_csv(str(src), str(dst)) 
    rows = read_csv_rows(dst) 
    assert len(rows) == 2 
    assert set(rows[0]) >= {"name", "age"} 


def test_csv_to_json_roundtrip(tmp_path: Path):
    '''тест конвертации из CSV в JSON'''
    src = tmp_path / "people.csv" 
    dst = tmp_path / "people.json" 
    src.write_text("name,age\nAlice,22\nBob,25\n", encoding="utf-8") 

    csv_to_json(str(src), str(dst)) 
    obj = json.loads(dst.read_text(encoding="utf-8")) 
    assert isinstance(obj, list) 
    assert len(obj) == 2 
    assert set(obj[0]) == {"name", "age"} 


def test_json_to_csv_empty_file(tmp_path: Path):
    '''Тест: пустой JSON файл должен вызывать ошибку'''
    src = tmp_path / "empty.json" 
    dst = tmp_path / "output.csv" 

    src.write_text("", encoding="utf-8") 

    with pytest.raises(ValueError): 
        json_to_csv(str(src), str(dst)) 


def test_csv_to_json_empty_file(tmp_path: Path):
    '''Тест: пустой CSV файл должен вызывать ошибку'''
    src = tmp_path / "empty.csv"
    dst = tmp_path / "output.json" 


    src.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        csv_to_json(str(src), str(dst)) 


def test_csv_to_json_only_headers(tmp_path: Path):
    '''Тест: CSV только с заголовками должен вызывать ошибку'''
    src = tmp_path / "headers_only.csv"  
    dst = tmp_path / "output.json" 

    src.write_text("name,age\n", encoding="utf-8")  

    with pytest.raises(ValueError): 
        csv_to_json(str(src), str(dst)) 


def test_missing_csv_raises():
    '''Тест: несуществующий CSV файл должен вызывать FileNotFoundError'''
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json") 


def test_missing_json_raises():
    '''Тест: несуществующий JSON файл должен вызывать FileNotFoundError'''
    with pytest.raises(FileNotFoundError):
        json_to_csv("nope.json", "out.csv")
