import sounddevice as sd

import numpy as np

import scipy.io.wavfile as wav

import speech_recognition as sr

gentoo = """
     -odNMMMMMMMMNNmhy+-`
   -yNMMMMMMMMMMMNNNmmdhy+-`
 `omMMMMMMMMMMMMNmdmmmmddhhy/`
 omMMMMMMMMMMMNhhyyyohmdddhhhdo`
.ydMMMMMMMMMMdhs++so/smdddhhhhdm+`
 oyhdmNMMMMMMMNdyooydmddddhhhhyhNd.
  :oyhhdNNMMMMMMMNNNmmdddhhhhhyymMh
    .:+sydNMMMMMNNNmmmdddhhhhhhmMmy
       /mMMMMMMNNNmmmdddhhhhhmMNhs:
    `oNMMMMMMMNNNmmmddddhhdmMNhs+`
  `sNMMMMMMMMNNNmmmdddddmNMmhs/.`
 /NMMMMMMMMNNNNmmmdddmNMNdso:`
+MMMMMMMNNNNNmmmmdmNMNdso/-`
yMMNNNNNNNmmmmmNNMmhs+/-`
/hMMNNNNNNNNMNdhs++/-`
`/ohdmmddhys+++/:.`
  `-//////:--`
"""



duration = 5

sample_rate = 44100

errores_max = 3

errores = 0

correctas = 0

words_by_level = {
    "facil": ["gato", "perro", "manzana", "leche", "sol"],
    "medio": ["banano", "escuela", "amigo", "ventana", "amarillo"],
    "dificil": ["tecnologia", "universidad", "informacion", "pronunciacion", "imaginacion"],
    "extremo": ["hola", "salsa inglesa", "coronel", "coro", "zona de trabajo"],
    "gentoo": [gentoo]
}

print("¡Bienvenido al juego de hablar!")
print("1. Se te mostrará una palabra en pantalla.")
print("2. Deberás pronunciar la palabra correctamente.")
print("3. Si pronuncias la palabra correctamente, ganaste, si no, cuenta un error")
print("4. El juego termina cuando cometes 3 errores.")
print("¡Buena suerte!")
nivel = input("Selecciona el nivel de dificultad (facil, medio, dificil, extremo): ")

if nivel == "facil":
    print("nivel facil (miedoso)")
    nivel = "facil"
elif nivel == "medio":
    print("nivel medio")
    nivel = "medio"
elif nivel == "dificil":
    print("nivel dificil")
    nivel = "dificil"
elif nivel == "extremo":
    print("nivel extremo (buena suerte)")
    nivel = "extremo"
elif nivel == "gentoo":
    print(gentoo)
    print("nivel gentoo (que Portage te acompañe)")
    nivel = "gentoo"
    raise SystemExit("Gentoo, no se habla, se compila...")
else:
    print(f"Nivel no válido, {nivel} seleccionando 'facil' por defecto.")
    nivel = "facil"

terminar = False

while not terminar:
    palabra = np.random.choice(words_by_level[nivel])
    print(f"Palabra: {palabra}")

    print("Habla ahora...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    wav.write("output.wav", sample_rate, recording)

    print("Grabación completa, ahora reconociendo...")

    recognizer = sr.Recognizer()
    recognize = recognize.lower()

    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        print(f"Has dicho: {text}")
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
        text = ""
    except sr.RequestError as e:
        print(f"Error al solicitar resultados del servicio de reconocimiento de voz; {e}")
        text = ""

    try:
        text = recognizer.recognize_google(audio, language="es-ES")
        print(f"Has dicho: {text}")
    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
        text = ""
    except sr.RequestError as e:
        print(f"Error al solicitar resultados del servicio de reconocimiento de voz; {e}")
        text = ""

    if text.lower() == palabra.lower():
        correctas += 1
        print("¡Correcto!")
    else:
        errores += 1
        print(f"No es correcto. Errores: {errores}/{errores_max}")
        if errores >= errores_max:
            print("Has alcanzado el número máximo de errores. Fin del juego.")
            terminar = True
            if correctas <= 0:
                print("No has acertado ninguna palabra. ¡Sigue practicando!")
            elif correctas <= 3:
                print("Has acertado algunas palabras. Pues... ¡Peor es nada!")
            elif correctas <= 5:
                print("¡Buen trabajo! Has acertado varias palabras.")
            elif correctas <= 10:
                print("¡Excelente! Has acertado muchas palabras.")
            else:
                print("¡Increíble! Has acertado demasiadas ¡Eres un maestro del habla!")
# gentoo :)