def calculate(lista):
    for i in range(len(lista)):
        if lista[i] % 2 != 0:
            lista[i] = lista[i] * 2
    return lista

def sort_tuple(lista_tupli):
    return sorted(lista_tupli, key=lambda x: x[1])

def replace_neg(lista):
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = 0
    return lista

def count(lista):
    dodatnie, ujemne = 0, 0
    for liczba in lista:
        if liczba >= 0:
            dodatnie += 1
        else:
            ujemne += 1
    return (dodatnie, ujemne)

def preprocess(znaki):
    liczba = 0
    for i in znaki:
        try:
            liczba = liczba * 10 + int(i)
        except:
            continue
    return liczba

def make_hashtags(lista):
    znaki = ""
    for word in lista:
        znaki += f"#{word} "
    return znaki.strip()

def convert_numbers(text):
    slownik = {'2': 'two','3': 'three'}
    slowa = text.split()
    for i in range(len(slowa)):
        if slowa[i] in slownik:
            slowa[i] = slownik[slowa[i]]
    return ' '.join(slowa)

def convert_text(text):
    tablica = text.split("_")
    for i in range(len(tablica)):
        tablica[i] = tablica[i][0].upper() + tablica[i][1:]
    wynik = "".join(tablica)
    return(wynik)

def convert_text_first(text):
    tablica = text.split("_")
    for i in range(1, len(tablica)):
        tablica[i] = tablica[i][0].upper() + tablica[i][1:]
    wynik = "".join(tablica)
    return(wynik)

def preprocess(lista):
    wynik = []
    for i in range(len(lista)):
        # Sprawdzamy, czy element listy ma rozszerzenie .png
        if lista[i].endswith("png"):
            wynik.append(lista[i])  # Dodajemy do wyników tylko element, nie całą listę
    return wynik