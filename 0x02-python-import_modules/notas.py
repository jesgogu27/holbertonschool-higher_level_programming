
def calificacion(nota):
	if nota == 5:
		print("La nota del alumno fue: {}".format(nota))


print("Programa Evaluacion de notas")
nota=input("Ingrese la nota: ")

calificacion(int(nota))