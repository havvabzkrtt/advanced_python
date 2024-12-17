# Her programlama dilinde regular expression kullanılabilir.
# Karmaşık bir metin içerisinde her hangi bir değer aramak için kullanılır.

import re

text = "BTK Akademi Python Dersleri BTK"
pattern = "BTK"

match = re.search(pattern, text) # text içerisinde bulunan ilk pattern döndürülür

sonuc = match
print(sonuc) # <re.Match object; span=(0, 3), match='BTK'>
# Match objesi döndürülüdü. match='BTK': eşleştirilen ifade, span=(0, 3): eşleşen ifade nerede
print(text[0:3]) # BTK

sonuc = match.start() # nerden başlar
print(sonuc) # 0

sonuc = match.end() # nerden biter
print(sonuc) # 3

match = re.findall(pattern, text) # tekrarlanan bütün patternleri döndürür
sonuc = match
print(sonuc) # ['BTK', 'BTK']
