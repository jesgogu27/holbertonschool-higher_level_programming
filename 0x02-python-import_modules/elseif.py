print("Verificar Edad")
edad = input("ingresar Edad:")

def paso(edad):
	if edad < 18:
		print("Usuario No Puede Pasar")
	else:
		print("Adelante")


paso(int(edad))

