import re

def normalize(text, *, casefold=True, yo2e=True):
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    if casefold:
        text = text.casefold()
    text = re.sub(r'[\t\r\n\f\v]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    return text.strip()

def tokenize(text):
    return re.findall(r'\b\w+(?:-\w+)*\b', text)

def count_freq(tokens):
    freq = {}
    for tok in tokens:
        freq[tok] = freq.get(tok, 0) + 1
    return freq

def top_n(freq, n=5):
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:n]

print(normalize("ПрИвЕт\nМИр\t"))             
print(normalize("ёжик, Ёлка"))                 
print(normalize("Hello\r\nWorld"))               
print(normalize(" двойные пробелы "))           

print(tokenize("привет мир"))                    
print(tokenize("hello,world!!!"))                 
print(tokenize("по-настоящему круто"))             
print(tokenize("2025 год"))                       
print(tokenize("emoji 😀 не слово"))              

freq = count_freq(["a","b","a","c","b","a"])
print(freq)                                        
print(top_n(freq, n=2))                           

freq = count_freq(["bb","aa","bb","aa","cc"])
print(top_n(freq, n=2))                            
