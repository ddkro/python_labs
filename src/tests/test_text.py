import pytest 
import sys
sys.path.append(r'C:\Users\User\Desktop\python_labs\src')
from lab3.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected", 
    [
        ("ПрИвЕт\nМИр\t", "привет мир"), 
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
def test_normalize_basic(source, expected):
    '''функция теста для normalize, берет данные из параметризации'''
    assert normalize(source) == expected 


@pytest.mark.parametrize( 
    "source,expected", 
    [
        ("привет мир", ["привет", "мир"]), 
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
    ],
)
def test_tokenize_basic(source, expected):
    '''функция теста для tokenize, берет данные из параметризации'''
    assert tokenize(source) == expected 


def test_count_freq_and_top_n():
    '''тест проверяет вместе функции count_freq и top_n'''
    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)
    assert freq == {"a": 3, "b": 2, "c": 1} 
    assert top_n(freq, 2) == [("a", 3), ("b", 2)] 
    assert top_n(freq, 0) == [] 
    assert top_n(freq, 5) == [("a", 3), ("b", 2), ("c", 1)] 
    assert count_freq([]) == {} 
    assert top_n({}, 5) == [] 


def test_top_n_tie_breaker():
    '''тест проверяет top_n с одинаковыми частотами'''
    freq = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert top_n(freq, 3) == [("aa", 2), ("bb", 2), ("cc", 1)]
