import math
#Exercise 1

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
dias = ('Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes')
nota= 3.6
año = 2025
precio = 21.50
temperatura_diaria = {
    'lunes': 20,
    'martes': 25,
    'miercoles': 15,
    'jueves': 18,
}

#Exercise 2
print(round(nota))
print(math.ceil(nota))

#Exercise 3
print(math.sqrt(nota))

#Exercise 4
print(list(temperatura_diaria.values())[0])
print(temperatura_diaria ['lunes'])

#Exercise 5
print(dias[1])

#Exercise 6
meses.append('Julio')
print(meses)

#Exercise 7
meses[0]='Diciembre'
print(meses)

#Exercise 8
meses.sort()
print(meses)

#Exercise 9
dias = dias + ('sábado',)
print(dias) 


