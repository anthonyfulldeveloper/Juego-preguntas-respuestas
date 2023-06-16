
preguntas = {
    "Cuál es el animal más grandel del mundo?": "La ballena azul",
    "¿Cuál es el planeta más cercano al Sol?": "Mercurio",
    "¿Qué animal tiene la piel a rayas negras y blancas?": "La cebra",
}

puntos = 0

for pregunta, respuesta in preguntas.items():
    print(pregunta)
    respuesta_usuario = input("Tu respuesta: ")

    if respuesta_usuario.lower() == respuesta.lower():
        print("¡Correcto!")
        puntos+=1
    else:
        print("Incorrecto, la respuesta correcta es: ",respuesta)
print(f"Finalizó el juego, obtuviste {puntos} puntos")