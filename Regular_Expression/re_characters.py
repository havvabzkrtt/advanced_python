import re

text = "A343a 123 XYZ 456 @&% 300 2 A343a 123456 1_2 abc"

# pattern = r"\d\d\d"  # 3 karakter, hepsi sayıl olacak
# pattern = r"\d+"  # \d : sayı içeriyor , + : bir ve üzeri sayıda eşleşme varsa, bütün sayıları döndürüyor
# pattern = r"\d*"   # * : 0 ve üzeri sayıda eşleşme varsa, boşluk karakterlerini de getirir çünkü sayı olmasa da döndürülüyor
# pattern = r"\d{3}"  # 3 karakterlileri getirir, 3 basamaklı sayıları getirir
# pattern = r"\d{3,5}" # min 3 max 5 basamaklıları getirir
# pattern = r"\d{3,}"  # min 3 basamaklıları getirir
# pattern = r"\d{,5}" # max 5 basamaklıları getirir, boşlukları da getirir
# pattern = r"\d.\d" # araya . eklenmesi : herhangi bir karakteri ifade eder, 3 karakterli ilk ve son karakter sayı ortadaki karakter herhangi bir karakter olabilir
# pattern = r"[a-zA-Z0-9]" # bütün her şeyi getirir
# pattern = r"\d|[a-z]"  # sayılar ya da "a" dan "z" ye olanları getirir
# pattern = r"\d\w\w\w"  # 4 basamaklı, ilk basamak sayı diğerleri \w : büyük küçük a dan z ye, sayılar ve alt çizgi içerenleri getirir
# pattern = r"^A\d\w\w\w"  # ^ : başlangıç karakterini belirler, A ile başlayacak
pattern = r"A\d\w\w\w$" # $ : sonuncu karakteri belirler

# matches = re.search(pattern, text)
# matches = re.findall(pattern, text)
matches = re.finditer(pattern, text)

for match in matches:
    print(match.group())

