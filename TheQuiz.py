import random
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PUNTUACIONES_PATH = os.path.join(BASE_DIR, "puntuaciones.json")
PREGUNTAS_PATH = os.path.join(BASE_DIR, "preguntas.json")
# Preguntas por niveles
with open(PREGUNTAS_PATH, 'r', encoding='utf-8') as f:
    levels = json.load(f)
levels["FIN"] = []


def seleccionar_preguntas(nivel):
    preguntas_disponibles = levels[nivel]
    if len(preguntas_disponibles) < 3:
        return preguntas_disponibles
    preguntas = random.sample(preguntas_disponibles, 3)
    random.shuffle(preguntas)
    return preguntas

def hacer_pregunta(pregunta):
    print("\n" + pregunta["texto"])
    for clave, valor in pregunta["opciones"].items():
        print(f"{clave}: {valor}")
    respuesta = input("Elige una opción (A, B, C, D): ").upper()
    return respuesta == pregunta["respuesta_correcta"]

def ver_puntuacion(usuario):
    if os.path.exists("puntuaciones.json"):
        with open("puntuaciones.json", "r") as f:
            data = json.load(f)
        if usuario in data:
            print(f"\n🧾 {usuario}, tu puntuación actual es: {data[usuario]} puntos")
        else:
            print(f"\n❌ No se encontró ninguna puntuación para {usuario}.")
    else:
        print("\n⚠️ No hay puntuaciones registradas todavía.")

def jugar():
    if not os.path.exists(PUNTUACIONES_PATH):
        with open(PUNTUACIONES_PATH, 'w') as f:
            json.dump({}, f)

    print("🎮 Bienvenido a The Quiz Game!")
    eleccion = input("¿Qué deseas hacer?\n1. Ver mi puntuación\n2. Jugar\nElige (1 o 2): ")

    usuario = input("Introduce tu nombre de usuario: ")

    if eleccion == "1":
        ver_puntuacion(usuario)
        seguir = input("\n¿Quieres jugar ahora? (s/n): ").lower()
        if seguir != "s":
            print("\n👋 ¡Hasta la próxima!")
            return

    puntuacion = 0
    nivel = 'beginner'

    with open(PUNTUACIONES_PATH, 'r') as f:
        data = json.load(f)

    while nivel != 'FIN':
        print(f"\n🌟 Nivel: {nivel}")
        preguntas = seleccionar_preguntas(nivel)
        for pregunta in preguntas:
            if hacer_pregunta(pregunta):
                print("✅ ¡Correcto!")
                puntuacion += 10
            else:
                print("❌ Incorrecto.")

        print(f"\n🧮 Puntuación total: {puntuacion}")

        if puntuacion >= 30 and nivel == 'beginner':
            nivel = 'intermediate'
            print("\n🚀 ¡Has avanzado al nivel intermedio!")
        elif puntuacion >= 60 and nivel == 'intermediate':
            nivel = 'advanced'
            print("\n🚀 ¡Has avanzado al nivel avanzado!")
        elif puntuacion >= 90 and nivel == 'advanced':
            nivel = 'pro'
        elif puntuacion >= 120 and nivel == 'pro':
            nivel = 'FIN'
            print("\n🏆 ¡Has alcanzado el nivel pro! El juego ha terminado.")
            break

        input("\nPresiona Enter para continuar...")

    data[usuario] = puntuacion

    with open(PUNTUACIONES_PATH, 'w') as f:
        json.dump(data, f)

    print(f"\n✅ Puntuación guardada para {usuario}. ¡Gracias por jugar!")

if __name__ == "__main__":
    jugar()
