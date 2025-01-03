def calculate_easy(tablica, k=5):
    wynik = []
    for i in range(1, len(tablica) - 1):
        if abs(tablica[i - 1] - tablica[i]) >= k \
            and abs(tablica[i + 1] - tablica[i]) >= k:
            wynik.append(tablica[i])
    return wynik   

def test_calculate_easy():
    print("Testing calculate_easy...")
    print(calculate_easy([2, 6, 2, 8, 1, 3, 10, 3]))
    print(calculate_easy([1, 6, 5, 2, 8, 11, 3, 10, 3], 3))
    print("test_calculate_easy: OK")

test_calculate_easy()
