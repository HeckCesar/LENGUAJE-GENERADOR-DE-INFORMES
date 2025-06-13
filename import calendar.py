import calendar

# ALMANAQUE DEL MES DE ABRIL

abril_dias = [
    "1 de abril - Día de las Bromas (April Fools' Day)",
    "7 de abril - Día Mundial de la Salud",
    "22 de abril - Día de la Tierra",
    "23 de abril - Día Internacional del Libro",
    "25 de abril - Día Mundial del Paludismo",
    "30 de abril - Día del Niño (en algunos países)"
]

def mostrar_almanaque():
    print("ALMANAQUE DEL MES DE ABRIL")
    print("-" * 30)
    for dia in abril_dias:
        print(dia)

def mostrar_calendario_abril_2025():
    print("\nCALENDARIO MES DE ABRIL 2025")
    print("-" * 30)
    print(calendar.month(2025, 4))

if __name__ == "__main__":
    mostrar_almanaque()
    mostrar_calendario_abril_2025()