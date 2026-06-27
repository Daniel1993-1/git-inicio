cantidad = int(input("ingresa el número de canciones para agregar: "))

if cantidad <= 0:
    print("debes agregar al menos una canción")
else:
    lista = []

    for i in range(cantidad):
        cancion = input(f"canción {i + 1}: ").strip().lower()
        lista.append(cancion)

    lista.sort()

    print("\n--- tu playlist ordenada ---")
    for i, cancion in enumerate(lista, start=1):
        print(f"{i}. {cancion}")
    print(f"\ntotal: {len(lista)} canciones")