def convertir_temperatura(valor, escala):
    try:
        valor = float(valor)
        if escala.lower() == "c":
            return f"{valor}°C equivale a {(valor * 9/5) + 32:.2f}°F"
        elif escala.lower() == "f":
            return f"{valor}°F equivale a {(valor - 32) * 5/9:.2f}°C"
        else:
            return "Escala inválida. Usa 'C' para Celsius o 'F' para Fahrenheit."
    except ValueError:
        return "Entrada inválida. Por favor, introduce un valor numérico."

def main():
    entrada_temp = input("Introduce la temperatura (por ejemplo, 25C o 77F): ")
    if entrada_temp[-1].lower() in ["c", "f"]:
        valor, escala = entrada_temp[:-1], entrada_temp[-1]
        print(convertir_temperatura(valor, escala))
    else:
        print("Formato inválido. Introduce un número seguido de 'C' o 'F'.")

if __name__ == "__main__":
    main()
##HECHO POR Juan Eduardo Pinilla Guzman T.I. 1097496453