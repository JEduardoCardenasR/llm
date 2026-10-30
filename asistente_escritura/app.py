"""
Asistente de escritura automática — Proyecto 1
Usa la API de OpenAI para corregir, continuar o generar texto.
"""

from openai import OpenAI

# Simulación de "configuración del sistema" (parte no crítica del software)
print("Iniciando asistente de escritura...")
print("Cargando preferencias de usuario (simulado)...\n")

api_key = input("Ingresa tu OpenAI API Key: ").strip()
if not api_key:
    print("Se necesita una API Key. Obtén una en https://platform.openai.com/api-keys")
    raise SystemExit(1)

client = OpenAI(api_key=api_key)


def preguntar_ia(instruccion: str, texto: str) -> str:
    """Envía un prompt a OpenAI y devuelve la respuesta."""
    respuesta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": instruccion},
            {"role": "user", "content": texto},
        ],
    )
    return respuesta.choices[0].message.content


def menu() -> None:
    while True:
        print("\n=== Asistente de Escritura ===")
        print("1. Corregir gramática y estilo")
        print("2. Sugerir continuación de un texto")
        print("3. Generar texto desde un tema")
        print("4. Salir")

        opcion = input("\nElige una opción (1-4): ").strip()

        if opcion == "1":
            texto = input("\nPega el texto a corregir:\n> ")
            print("\nCorrigiendo...")
            resultado = preguntar_ia(
                "Corrige la gramática, ortografía y estilo del texto. "
                "Devuelve solo el texto corregido, en el mismo idioma.",
                texto,
            )
            print("\n--- Texto mejorado ---\n")
            print(resultado)

        elif opcion == "2":
            texto = input("\nEscribe el inicio del texto:\n> ")
            print("\nGenerando sugerencia...")
            resultado = preguntar_ia(
                "Continúa el siguiente texto de forma coherente. "
                "Escribe solo la continuación (un párrafo).",
                texto,
            )
            print("\n--- Continuación sugerida ---\n")
            print(resultado)

        elif opcion == "3":
            tema = input("\n¿Sobre qué tema quieres escribir?\n> ")
            tono = input("Tono (profesional / casual / creativo / persuasivo): ").strip() or "profesional"
            print("\nEscribiendo...")
            resultado = preguntar_ia(
                f"Eres un asistente de escritura. Redacta un texto completo "
                f"con tono {tono}. Devuelve solo el texto.",
                f"Tema: {tema}",
            )
            print("\n--- Texto generado ---\n")
            print(resultado)

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
