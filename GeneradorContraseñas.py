import random

print("Este es un generador de contraseñas aleatorias")
characters = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ!@€$%^&*().,?¿¡'·|0123456789"

amount = int(input("Cuantas contraseñas quieres generar? Pon solo números: "))

lenght = int(input("¿Cuántos caracteres quieres que tenga cada contraseña? Pon solo números: "))

print("\nEstas son tus contraseñas:")

for i in range(amount):
    passwords = ""
    
    for j in range(lenght):
        passwords  += random.choice(characters)
    print(passwords)


