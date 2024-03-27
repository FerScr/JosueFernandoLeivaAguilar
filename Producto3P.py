import requests

def search_books_title(titulo):
    url = f"https://openlibrary.org/search.json?title={titulo}"
    response = requests.get(url)
    data = response.json()
    return data

def search_books_author(autor):
    url = f"https://openlibrary.org/search.json?author={autor}"
    response = requests.get(url)
    data = response.json()
    return data

def search_books_genre(genero):
    url = f"https://openlibrary.org/subjects/{genero.lower()}.json"
    response = requests.get(url)
    data = response.json()
    return data

def menu():
    while True:
        print()
        print("Bienvenido a la biblioteca digital")
        print("1. Buscar por titulo")
        print("2. Buscar por autor")
        print("3. Buscar por género")
        print("4. Salir del programa")
        sel = input("Ingresa una opción: ")

        if sel == '1':
            titulo = input("Ingresa el título del libro que deseas buscar: ")
            res = search_books_title(titulo)
            display_results(res)
        elif sel == '2':
            autor = input("Ingresa el nombre del autor que deseas buscar: ")
            res = search_books_author(autor)
            display_results(res)
        elif sel == '3':
            genero = input("Ingresa el género del libro que deseas buscar: ")
            res = search_books_genre(genero)
            display_results(res)
        elif sel == '4':
            print("Nos vemos pronto...")
            break
        else:
            print("Opcion invalida, intenta nuevamente")
        
        print()

def display_results(res):
    if res and 'docs' in res:
        print()
        print("Resultados encontrados:")
        for book in res['docs']:
            print("Titulo:", book.get('title', 'No disponible'))
            print("Autor:", ", ".join(book.get('author_name', ['No disponible'])))
            print()
    elif res and 'works' in res:
        print()
        print("Resultados encontrados:")
        for book in res['works']:
            print("•", book.get('title', 'No disponible'))
    else:
        print("No se encontraron resultados.")

if __name__ == "__main__":
    menu()
