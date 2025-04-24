"""Interfaz para enviar consultas a la API de OpenAI usando ChatGPT."""

import readline  # pylint: disable=unused-import
import openai

openai.api_key = "TU_API_KEY"


def obtener_consulta():
    """Solicita y valida una consulta del usuario."""
    try:
        consulta = input("Ingrese su consulta: ").strip()
        if not consulta:
            print("La consulta no puede estar vacía.")
            return None
        print("You:", consulta)
        return consulta
    except (EOFError, KeyboardInterrupt) as e:
        print("Error al ingresar la consulta:", e)
        return None


def enviar_a_chatgpt(mensaje):
    """Envía la consulta a la API de ChatGPT y muestra la respuesta."""
    try:
        respuesta = openai.ChatCompletion.create(  # pylint: disable=no-member
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": mensaje}]
        )
        texto = respuesta.choices[0].message['content']
        print("chatGPT:", texto)
    except openai.error.OpenAIError as e:  # pylint: disable=no-member
        print("Error al contactar la API:", e)


def main():
    """Ciclo principal de interacción con el usuario."""
    print("Presioná ↑ (flecha arriba) para recuperar la última consulta.")
    while True:
        try:
            consulta = obtener_consulta()
            if consulta:
                enviar_a_chatgpt(consulta)
        except KeyboardInterrupt:
            print("\nSaliendo del programa.")
            break


if __name__ == "__main__":
    main()
