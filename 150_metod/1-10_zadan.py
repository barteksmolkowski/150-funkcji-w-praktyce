listy = []
def is_nested(listy):
    if not listy:
        return False
    for i in range(len(listy)):
        if type(listy[i]) != list:
            return False
    return True

lista = []
def is_all_equal(lista):
    zmienna = lista[0]
    for i in range(len(lista)):
        if lista[i] != zmienna:
            return False
    return True

def is_valid_array(macierz):
    if macierz == None:
        return True
    else:
        for i in range(len(macierz)):
            if type(macierz[i]) != list:
                return False
        dlugosc_wiersza = len(macierz[0])
        for i in range(len(macierz)):
            if len(macierz[i]) != dlugosc_wiersza:
                return False
        return True

def swap_elements_easy(lista):
    ostatnia = lista[len(lista) - 1]
    lista.remove(ostatnia)
    lista.append(lista[0])
    lista[0] = ostatnia
    return lista

def swap_elements_hard(lista, index1, index2):
    zmiana = lista[index1]
    lista[index1] = lista[index2]
    lista[index2] = zmiana
    return lista

def reverse_words(tekst):
    tablica = []
    slowo = ""
    for i in range(len(tekst)):
        if tekst[i] == " ":
            tablica.append(slowo)
            slowo = ""
        else:
            slowo += tekst[i]
        if i == len(tekst) - 1:
            tablica.append(slowo)

    n_tablica = []
    i = len(tablica) - 1
    while i >= 0:
        n_tablica.append(tablica[i])
        i -= 1

    return " ".join(n_tablica)

def test_is_nested():
    print("Funkcja 'is_nested' sprawdza, czy wszystkie elementy w liście są listami.")
    print("\nTest: [[1, 2], [3, 4]]")
    print(is_nested([[1, 2], [3, 4]]))  
    print("\nTest: [[1, 2], 3]")
    print(is_nested([[1, 2], 3]))        
    print("\nTest: []")
    print(is_nested([]))                 
    print("\nTest: [1, 2, 3]")
    print(is_nested([1, 2, 3]))          

def test_is_all_equal():
    print("\nFunkcja 'is_all_equal' sprawdza, czy wszystkie elementy w liście są równe.")
    print("\nTest: [1, 1, 1]")
    print(is_all_equal([1, 1, 1]))       
    print("\nTest: [1, 2, 1]")
    print(is_all_equal([1, 2, 1]))       
    print("\nTest: [3]")
    print(is_all_equal([3]))             

def test_is_valid_array():
    print("\nFunkcja 'is_valid_array' sprawdza, czy lista jest poprawną macierzą (czy wszystkie wiersze mają taką samą długość).")
    print("\nTest: [[1, 2], [3, 4]]")
    print(is_valid_array([[1, 2], [3, 4]]))   
    print("\nTest: [[1, 2], [3]]")
    print(is_valid_array([[1, 2], [3]]))       
    print("\nTest: [1, 2, 3]")
    print(is_valid_array([1, 2, 3]))           
    print("\nTest: None")
    print(is_valid_array(None))                

def test_swap_elements_easy():
    print("\nFunkcja 'swap_elements_easy' zamienia pierwszy i ostatni element w liście.")
    lista = [1, 2, 3, 4]
    print("\nTest: [1, 2, 3, 4]")
    print(swap_elements_easy(lista))         

def test_swap_elements_hard():
    print("\nFunkcja 'swap_elements_hard' zamienia elementy listy pod wskazanymi indeksami.")
    lista = [1, 2, 3, 4]
    print("\nTest: [1, 2, 3, 4], indeksy: 0, 3")
    print(swap_elements_hard(lista, 0, 3))    

def test_reverse_words():
    print("\nFunkcja 'reverse_words' odwraca kolejność słów w tekście.")
    tekst = "Hello world przykład"
    print("\nTest: 'Hello world przykład'")
    print(reverse_words(tekst))              

# Testy funkcji
print("Testy:\n")
test_is_nested()
test_is_all_equal()
test_is_valid_array()
test_swap_elements_easy()
test_swap_elements_hard()
test_reverse_words()

def remove_common_elements(tablica1, tablica2):
    if len(tablica1) > len(tablica2):
        tablica1, tablica2 = tablica2, tablica1

    for element in tablica2:
        while element in tablica1:
            tablica1.remove(element)
    return tablica1, tablica2

remove_common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6])

data = [
    {'user': 'joe', 'main_technology': 'python'},
    {'user': 'tom', 'main_technology': 'c/cpp'},
    {'user': 'michael', 'main_technology': 'cloud'},
    {'user': 'bob', 'main_technology': 'php'},
    {'user': 'lil', 'main_technology': 'html'},
    {'user': 'alice', 'main_technology': 'sql'},
]

def convert(data):
    slownik = {"user":[], "main_technology":[]}
    for i in range(len(data)):
        slownik["user"].append(data[i]["user"])
        slownik["main_technology"].append(data[i]["main_technology"])

    return slownik

print(convert(data))

def get_indices_easy(tablica, element):
    indeksy = []
    for i in range(len(tablica)):
        if tablica[i] == element:
            indeksy.append((i))
    return indeksy

print(get_indices_easy([1, 2, 3], 2))

def get_indices_hard(tablica):
    indeksy = []
    for i in range(len(tablica)):
        if type(tablica[i]) == str:
            indeksy.append(i)
    return indeksy

print(get_indices_easy([1, 2, 3], 2))
