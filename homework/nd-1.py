import requests  # Importuojame requests biblioteką, kuri leidžia vykdyti HTTP užklausas

# Nuskaitome duomenis iš API
response = requests.get("https://jsonplaceholder.typicode.com/todos")  
# Išsiunčiame GET užklausą į nurodytą API adresą, kad gautume duomenis

# Patikriname, ar užklausa buvo sėkminga
if response.status_code == 200:  
    # Jei HTTP atsakymo kodas yra 200, tai reiškia, kad užklausa pavyko
    
    todos = response.json()  # Konvertuojame JSON duomenis į Python sąrašą (list)
    
    for todo in todos[:10]:  # Ciklas eina per pirmas 10 užduočių
        print(f"ID: {todo['id']}, Pavadinimas: {todo['title']}, Atlikta: {todo['completed']}")
        # Atspausdiname kiekvienos užduoties ID, pavadinimą ir atlikimo būseną
else:
    print("Nepavyko gauti duomenų iš API")  
    # Jei užklausa nepavyko, išvedame klaidos pranešimą

# ats.
# ID: 1, Pavadinimas: delectus aut autem, Atlikta: False
# ID: 2, Pavadinimas: quis ut nam facilis et officia qui, Atlikta: False
# ID: 3, Pavadinimas: fugiat veniam minus, Atlikta: False
# ID: 4, Pavadinimas: et porro tempora, Atlikta: True
# ID: 5, Pavadinimas: laboriosam mollitia et enim quasi adipisci quia provident illum, Atlikta: False
# ID: 6, Pavadinimas: qui ullam ratione quibusdam voluptatem quia omnis, Atlikta: False
# ID: 7, Pavadinimas: illo expedita consequatur quia in, Atlikta: False
# ID: 8, Pavadinimas: quo adipisci enim quam ut ab, Atlikta: True
# ID: 9, Pavadinimas: molestiae perspiciatis ipsa, Atlikta: False
# ID: 10, Pavadinimas: illo est ratione doloremque quia maiores aut, Atlikta: True
