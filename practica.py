print("Hola Morenito papasote bello")
edad = int(input("Ingresa tu edad: "))

if 0 < edad <= 12:
    print("Eres un niño.")
elif 12 < edad < 18:
    print("Eres un adolescente.")
elif 18 <= edad < 50:
    print("Eres un adulto.")
else:
    print("Eres una persona mayor.")
