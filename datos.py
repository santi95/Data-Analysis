import collections
from functools import *
import errores

Person = collections.namedtuple('persona', 'num, nombre, apellido, genoma')
lista_datos = collections.namedtuple('lista_datos', 'id_lista, numeros')
Person2 = collections.namedtuple('persona', 'num, nombre, apellido, diccionario_genes')

def leer_listas():
    parser = lambda line: line.rstrip('\n').split(";")
    with open('listas.txt', 'r', encoding = 'utf-8') as file1:
        lista = [lista_datos(*(parser(line))) for line in file1]
    return lista

def obtener_numero_inicial(data):
    try:
        ln = data[0]
        if (data[1]).isnumeric():
            ln1 = data[1]
            ln = ln + ln1
        return int(ln)
    except errores.GenomeError(data):
        pass

def obtener_numero_secundario(data, ln):
    try:
        largo = len(str(ln))
        la = data[int(ln) + largo]
        if (data[int(ln) + 1 + largo]).isnumeric():
            la1 = data[int(ln)+ largo + 1]
            la  = la + la1
        posi = int(ln) + len(str(la)) + largo
        posj = int(ln) + int(la) + len(str(la)) + largo
        return (int(posi), int(posj))
    except errores.GenomeError(data):
        pass

gen_lista = collections.namedtuple('gen_lista', 'gen, numero')



def obt_numeros(string, num, nombre, apellido):
    try:
        pos_numeros = [s for s in range(len(string)) if string[s].isnumeric()]
        pos_numeros.append(0)
        numero_x_gen = [string[pos_numeros[x]]+ (string[pos_numeros[x+1]]
                        if int(pos_numeros[x]) + 1 == int(pos_numeros[x+1]) else "")
                        for x in range(len(pos_numeros)-1)
                        if int(pos_numeros[x-1] + 1) != pos_numeros[x]]
        string = [string[s] for s in range(len(string)) if string[s].isnumeric() == False]
        if ('B','D','D','F','H','I','J','K','L','M','N','O','P','Q','R','S','U','V','W','X','Y','Z') in string:
            raise errores.GenomeError("".join(string))
        string = ('').join(string) ; string1 = string[27:]
        string = list(map(''.join, zip(*[iter(string)]*3)))
        string1 = list(map(''.join, zip(*[iter(string1)]*3)))
        genoma = [gen_lista(string[x], numero_x_gen[x]) for x in range(9)]
        matriz_genes_personas.append(genoma)
        personas.append(Person(num, nombre, apellido, string1))
    except errores.GenomeError(string):
        print("No hay números en esta linea del genoma")

def arreglar_lista_asociados(pos):
    if pos < len(lista):
        obj = lista[pos]
        id = obj.id_lista
        futura_lista = obj.numeros
        futura_lista = futura_lista[1:]
        lista1 = futura_lista.split(',')
        listas.append(lista_datos(id, lista1))
        arreglar_lista_asociados(pos+1)

def generador_lista_genes(x,y, dict1):
    if y < 9 and x < len(personas):
        id_gen_x = matriz_genes_personas[x][y].numero
        gen_x = matriz_genes_personas[x][y].gen
        lista_gen_x = [num.numeros for num in listas if num.id_lista == id_gen_x ][0]
        try:
            lista_genes = [personas[x].genoma[int(num)] for num in lista_gen_x]
            dict1.update({gen_x: lista_genes})
        except:
            dict1.update({gen_x: ''})
        y += 1 ; generador_lista_genes(x,y, dict1)
    elif y >= 9 and x < len(personas):
        personas_genotipo.append(Person2(x, personas[x].nombre, personas[x].apellido, dict1))
        x += 1 ; y = 0
        generador_lista_genes(x,y, {})

def leer_datos(data, num):
    if data != None:
        ln = obtener_numero_inicial(data)
        largo = len(str(ln))
        tupla = obtener_numero_secundario(data, ln)
        nombre1 = data[largo:ln+largo]
        apellido1 = data[tupla[0]:tupla[1]]
        genoma1 = data[tupla[1]:]
        obt_numeros(genoma1, num, nombre1, apellido1)
        data = next(temp, None)
        leer_datos(data, num + 1)


personas = []
matriz_genes_personas = []
personas_genotipo = []
listas = []

try:
    #Lectura Listas
    lista = leer_listas()
    #Lectura Archivo
    file = open('genomas.txt', 'r', encoding = 'utf-8')
    temp = (line.strip() for line in file)
    data = next(temp)
    leer_datos(data, 0)
    arreglar_lista_asociados(0)
    generador_lista_genes(0,0,{})

except errores.GenomeError():
    pass

# for i in range(len(personas_genotipo)):
#     print(personas_genotipo[i])
