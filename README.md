# Kalkulator

[![Pylint](https://github.com/BerSecHub/calculator/actions/workflows/pylint.yml/badge.svg?branch=main)](https://github.com/BerSecHub/calculator/actions/workflows/pylint.yml)
[![Python application](https://github.com/BerSecHub/calculator/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/BerSecHub/calculator/actions/workflows/python-app.yml)

Kalkulator dwóch liczb przygotowany w ramach laboratorium 2. Klasa `Calculator(op1, op2)` udostępnia metody `sum()`, `subtract()`, `multiply()` i `divide()`.
Żadna metoda nie zgłasza wyjątku. Dla nieprawidłowych argumentów (tekst, `None`, lista, liczba całkowita za duża dla typu float) oraz przy dzieleniu przez zero wynikiem jest `nan`.

## Gdzie znaleźć poszczególne części laboratorium

| Wymaganie z konspektu | Gdzie |
|---|---|
| Klasa zgodna z diagramem UML, przypadki szczególne, przykłady wywołania | [`calculator.py`](calculator.py) |
| Testy jednostkowe (14 przypadków, w tym testy parametryzowane) | [`test_calculator.py`](test_calculator.py) |
| 100% pokrycia testami, raport w głównym katalogu | [`coverage_report.txt`](coverage_report.txt), [`htmlcov/`](htmlcov/) |
| `.gitignore` | [`.gitignore`](.gitignore) |
| Pylint 10/10 | odznaka powyżej, [`pylint.yml`](.github/workflows/pylint.yml) (Python 3.12, 3.13, 3.14) |
| GitHub Actions z pokryciem testami | [`python-app.yml`](.github/workflows/python-app.yml): flake8, testy, próg pokrycia `--fail-under=100`, raport HTML jako artefakt |
| Hook pre-commit z Pylintem | [`.pre-commit-config.yaml`](.pre-commit-config.yaml) |
| GitHub Projects, zadanie zamknięte automatycznie commitem | [Projects](https://github.com/BerSecHub/calculator/projects), [issue #1](https://github.com/BerSecHub/calculator/issues/1) zamknięte w [`7d90e36`](https://github.com/BerSecHub/calculator/commit/7d90e36) |
| Odznaki statusu obu akcji | początek tego pliku |
| Zepsuty test, odrzucony push, pull, push | [`855a625`](https://github.com/BerSecHub/calculator/commit/855a625) |
| Gałąź, test parametryzowany, pull request, scalenie | [pull request #3](https://github.com/BerSecHub/calculator/pull/3), commit scalający [`488197d`](https://github.com/BerSecHub/calculator/commit/488197d) |
| Testy interfejsu w Playwright | [`test_playwright.py`](test_playwright.py) (4 testy strony Wydziału Informatyki AGH) |
| venv, pip, `requirements.txt`, uv | [`requirements.txt`](requirements.txt) (generowany z `uv.lock`), [`pyproject.toml`](pyproject.toml), [`uv.lock`](uv.lock) |

## Jak uruchomić

Za pomocą [uv](https://docs.astral.sh/uv/):

```bash
uv sync                                   # tworzy .venv i instaluje zależności z uv.lock
uv run python calculator.py               # przykłady wywołania
uv run pytest test_calculator.py          # testy jednostkowe
uv run coverage run -m pytest test_calculator.py
uv run coverage report -m                 # raport pokrycia
uv run pylint $(git ls-files '*.py')      # analiza statyczna
uv run playwright install                 # przeglądarki dla testów Playwright
uv run pytest test_playwright.py          # testy interfejsu (żywa strona)
uv run pre-commit install                 # włączenie hooka pre-commit
```

Za pomocą pip:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Odpowiedzi na pytania z konspektu

### 1. Jak zaimplementować prywatne pola i funkcje?

Python nie ma modyfikatorów dostępu. Dwa podkreślniki na początku nazwy włączają zmianę nazwy (name mangling): wewnątrz klasy `self.__op1` staje się `self._Calculator__op1`, więc poza klasą `calc.__op1` zgłasza `AttributeError`. Jeden podkreślnik to tylko umowa między programistami. Zmiana nazwy chroni przed przypadkowym użyciem i przed kolizją nazw w klasach dziedziczących, ale nie jest zabezpieczeniem: `calc._Calculator__op1` nadal działa.

### 2. Na co zwrócił uwagę Pylint?

- Brak docstringów modułu, klasy i metod (`C0114`, `C0115`, `C0116`).
- Zbędne `else` po `return` (`R1705`).
- Brak znaku nowej linii na końcu pliku (`C0304`).
- Przecinek po docstringu, który zamienił go w krotkę (`W0104`, instrukcja bez efektu).
- `E1101` (brak atrybutu), gdy przykłady wywoływały metody o nazwach niezgodnych z diagramem UML. Pylint znalazł ten błąd bez uruchamiania kodu.
- W GitHub Actions: `E0401` (błąd importu), gdy w `requirements.txt` brakowało pakietu.

Wszystkie uwagi są poprawione, a wynik to 10.00/10.

### 3. Czym różni się kontrola przez pre-commit od kontroli w GitHub Actions i po co stosować obie?

- **pre-commit** działa lokalnie, przed utworzeniem commita. Informacja przychodzi w kilka sekund, a błędny kod nie trafia do historii. Działa jednak tylko u osób, które zainstalowały hook, i da się go pominąć (`git commit --no-verify`).
- **GitHub Actions** działa na czystej maszynie po każdym pushu i dla każdego pull requesta. Obowiązuje wszystkich, nie da się go pominąć, a wynik widać publicznie (odznaki, wyniki przy pull requestach). Informacja przychodzi dopiero po pushu.
- **Obie naraz** dają szybką informację lokalnie i gwarancję na serwerze, pod warunkiem że progi są takie same. Przy `--fail-under=8.0` prawdziwy błąd (`E1101`, wynik 8.28/10) przechodził przez hook, a akcja Pylint by go odrzuciła. Dlatego hook używa `--fail-under=10`.

### 4. Co się stało przy wysyłaniu zepsutego testu i dlaczego?

Push został odrzucony (`! [rejected] main -> main (fetch first)`), bo commity z README powstały na GitHubie i nie było ich w lokalnym repozytorium. Git nie nadpisuje historii na serwerze. `git pull --rebase` przeniósł lokalny commit na szczyt commitów z serwera i kolejny push się udał.

Hook pre-commit nie zatrzymał zepsutego testu, bo Pylint nie uruchamia testów. Akcja Python application zakończyła się błędem (`assert 5.0 == 6`), a jej odznaka pokazała „failing”. Test został naprawiony na gałęzi `fix-test` i scalony przez pull request #3.

### 5. Dlaczego przy pisaniu testów warto używać trybu headed, a w CI wystarcza tryb headless?

Tryb headed pokazuje, co test naprawdę robi. To pomaga przy pisaniu i poprawianiu lokatorów, razem z `PWDEBUG=1` i Playwright Inspectorem. Serwery CI nie mają ekranu, a tryb headless jest szybszy i zużywa mniej pamięci.

### 6. Czy kod nagrany przez `playwright codegen` można wykorzystać bezpośrednio jako test?

Nie. Nagranie zawiera tylko czynności, bez asercji, więc przeszłoby nawet wtedy, gdy kliknięcie prowadzi na złą stronę. Trzeba uzupełnić:

- asercje `expect`, np. że nagłówek jest widoczny albo że adres się zmienił;
- stabilne lokatory: role i nazwy elementów oraz ograniczenie wyszukiwania do menu nawigacji, żeby uniknąć błędu strict mode violation;
- obsługę rozwijanych menu.

Testy sprawdzają zachowanie widoczne dla użytkownika, a nie szczegóły HTML, bo strona się zmienia. Przykład: pozycja „Dydaktyka” zniknęła z menu.