import itertools

def concat_easy(tablica1, tablica2):
    nowa_tab = []
    for i in range(min(len(tablica1), len(tablica2))):
        nowa_tab.append(tablica1[i] + tablica2[i])
    if len(tablica1) > len(tablica2):
        nowa_tab.extend(tablica1[len(tablica2):])
    elif len(tablica2) > len(tablica1):
        nowa_tab.extend(tablica2[len(tablica1):])
    return nowa_tab

def concat_hard(tablica1, tablica2):
    if len(tablica1) != len(tablica2):
        raise ValueError('The given lists are not of the same length.')
    
    nowa_tab = []
    for i in range(min(len(tablica1), len(tablica2))):
        nowa_tab.append(tablica1[i] + tablica2[i])
    if len(tablica1) > len(tablica2):
        nowa_tab.extend(tablica1[len(tablica2):])
    elif len(tablica2) > len(tablica1):
        nowa_tab.extend(tablica2[len(tablica1):])
    return nowa_tab

def sort_by_row(lista):
    def sort(lst):
        for i in range(len(lst)):
            for j in range(len(lst) - 1):
                if lst[j] > lst[j + 1]:
                    zmiana = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = zmiana
        return lst
    
    n_lista = []
    for i in range(len(lista)):
        n_lista.append(sort(lista[i]))
    return n_lista

def top3(data):
    
    def sort(lst):
        for i in range(len(lst)):
            for j in range(len(lst) - 1):
                if lst[j] > lst[j + 1]:
                    zmiana = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = zmiana
        return lst
    
    def three_max(lista):
        if len(lista) < 3:
            return sorted(lista, reverse=True)
        wartosci = []
        for i in range(3):
            max_value = max(lista)
            wartosci.append(max_value)
            lista.remove(max_value)
        return sorted(wartosci, reverse=True)
    
    result = []

    for i in range(len(data)):
        wiersz = data[i]
        wiersz = sort(wiersz)
        wiersz = three_max(wiersz)
        result.append(wiersz)
    
    return result

def filter_users(user_data):
    user_level_data = []
    for i in range(len(user_data)):
        if "level" in user_data[i]:
            user_level_data.append(user_data[i])
    return user_level_data

def remove_repetitive(numbers):
    def has_repetitive_digits(number):
        digits = str(number)
        return len(digits) != len(set(digits))
    
    result = []
    for number in numbers:
        if not has_repetitive_digits(number):
            result.append(number)
    return result

def calculate_easy(lista, k=5):#źle?
    wynik = []
    for i in range(1, len(lista) - 1):
        if abs(lista[i] - lista[i - 1]) >= k or abs(lista[i] - lista[i + 1]) >= k:
            wynik.append(lista[i])
    return wynik

def calculate_hard(zdanie):
    slowa = zdanie.split()
    permutacje = list(itertools.permutations(slowa))
    return [' '.join(perm) for perm in permutacje]

def create_mask(lista1, lista2):
    maska = []
    for i in range(len(lista1)):
        if lista1[i] == lista2[i]:
            maska.append(1)
        else:
            maska.append(0)
    return maska

def distance(lista1, lista2):
    0