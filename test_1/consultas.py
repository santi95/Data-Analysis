from parentesco import par_neg, par_0, par_1, par_2, par_n
from proceso import *
from collections import Counter
from functools import reduce
from datos import personas_genotipo
import errores

def ascendencia(id):
    lis_asc = []
    per = feno_final[id]
    gen = feno[id].diccionario_genes
    if per.color_pelo == 'Negro' and 'Pecho' in per.vello and per.nariz == 'Recta':
        lis_asc.append('Mediterránea')
    if per.tono == 'Negro' and per.color_pelo == 'Negro' and per.pies > 44:
        lis_asc.append('Africana')
    if per.guata[0] == 'Guatón Parrillero' and 'Espalda' in per.vello:
        lis_asc.append('Estadounidense')
    if 'AAT' in gen['GTC'] and 'AAT' in gen['GGA'] and 'AAT' in gen['TCT']:
        lis_asc.append("Albina")

    # if lis_asc == []:
    #     raise errores.NotAcceptable('Ascendencia Vacía')

    return lis_asc

def índice_de_tamaño(id):
    geno = feno[id].diccionario_genes['AAG']            #tamaño
    counter = Counter(geno)
    chicos = counter['ACT']
    grandes = counter['AGT']
    total = chicos + grandes
    porc = grandes/total
    geno1 = feno[id].diccionario_genes['TGG']           #Guata
    counter1 = Counter(geno1)
    chicos1 = counter1['ACT']
    grandes1 = counter1['AGT']
    total1 = chicos1 + grandes1
    porc1 = grandes1/total1
    if total == 0 or total1 == 0:
        raise errores.NotAcceptable("Indice de Tamaño sin gen especificado")
    return (porc*porc1)**(1/2)

def pariente_de(grado, id):   #En vez de listas hacerlos generadores
    try:
        if grado == -1:
            primos = [feno_final[i].nombre + " " + feno_final[i].apellido
                      for i in range(len(feno_final))
                      if par_neg(id, i) == True and i != id]
            return primos
        if grado == 0:
            geno_igual = [feno_final[i].nombre + " " + feno_final[i].apellido
                          for i in range(len(feno_final))
                          if par_0(id,i) == True and i != id]
            return geno_igual
        if grado == 1:
            geno_parecido1 = [feno_final[i].nombre + " " + feno_final[i].apellido
                              for i in range(len(feno_final))
                              if i != id and par_1(id,i) == True]
            return geno_parecido1
        if grado == 2:
            geno_parecido2 = [feno_final[i].nombre + " " + feno_final[i].apellido
                              for i in range(len(feno_final))
                              if par_2(id,i) == True and i != id]
            return geno_parecido2
        if grado == 'n':
            geno_parecidon = [feno_final[i].nombre + " " + feno_final[i].apellido
                              for i in range(len(feno_final))
                              if par_n(id,i) == True and i != id]
            return geno_parecidon
    except errores.NotFound("Atributos incorrectos para pedir los parientes de una persona"):
        pass


def id_getter(nombre_completo):
    try:
        n = nombre_completo.split(" ", 1)
        nombre = n[0]
        apellido = n[1]
        id = [feno_final[i].id for i in range(len(feno_final))
              if feno_final[i].nombre == nombre and feno_final[i].apellido == apellido]
        return int(id[0])
    except:
        errores.NotFound("No se encontró el nombre pedido")
def get_counter(id):
    try:
        lista = personas_genotipo[id].diccionario_genes
        counter = [Counter(lista[i]) for i in lista]
        return counter
    except errores.NotFound("El id no es válido"): pass

def gemelo_genetico(id):
    counters = [get_counter(i) for i in range(len(personas_genotipo))]
    c_cool = counters[id]


def valor_característica(tag_identificador, nombre_completo):
    # GTC, nombre
    try:
        id = id_getter(nombre_completo)
    except errores.NotFound("El nombre no es válido"):
        pass
    if tag_identificador == 'AAG': return feno_final[id].altura
    if tag_identificador == 'GTC': return feno_final[id].color_ojos
    if tag_identificador == 'GGA': return feno_final[id].color_pelo
    if tag_identificador == 'TCT': return feno_final[id].tono
    if tag_identificador == 'GTA': return feno_final[id].nariz
    if tag_identificador == 'CTC': return feno_final[id].pies
    if tag_identificador == 'CGA': return feno_final[id].vello
    if tag_identificador == 'TGG': return feno_final[id].guata
    if tag_identificador == 'TAG': return feno_final[id].vision

def solo_carac(x):
    carac = [i for i in feno_final[x]]
    return carac[3:]

def tag_num(tag_caracteristica):
    if tag_caracteristica == 'AAG': return 0    #altura
    if tag_caracteristica == 'GTC': return 1
    if tag_caracteristica == 'GGA': return 2
    if tag_caracteristica == 'TCT': return 3
    if tag_caracteristica == 'GTA': return 4
    if tag_caracteristica == 'CTC': return 5     #pies
    if tag_caracteristica == 'TGG': return 6
    if tag_caracteristica == 'CGA': return 7
    if tag_caracteristica == 'TAG': return 8

def min(tag_caracteristica):
    try:
        car_x = tag_num(tag_caracteristica)
        if car_x == 0 or car_x == 5:
            car = [float(solo_carac(i)[car_x]) for i in range(len(feno_final))]
            car.sort() ; return car[0]
        else:
            car = (solo_carac(i)[car_x] for i in range(len(feno_final)))
            count = Counter(car)
            mini = count.most_common()[:-len(count):-1] ; return mini[0][0]
    except errores.NotFound("El tag no existe"): pass

def max(tag_caracteristica):
    try:
        car_x = tag_num(tag_caracteristica)
        if car_x == 0 or car_x == 5:
            lista = [float(solo_carac(i)[car_x]) for i in range(len(feno_final))]
            lista.sort() ; return lista[len(lista)-1]
        else:
            carac = (solo_carac(i)[car_x] for i in range(len(feno_final)))
            count = Counter(carac)
            maxi = count.most_common() ; return maxi[0][0]
    except errores.NotFound("El tag no existe"): pass

def prom(tag_caracteristica):
    car_x = tag_num(tag_caracteristica)
    if car_x == 0 or car_x == 5:
        gen = (float(solo_carac(i)[car_x]) for i in range(len(feno_final)))
        total = reduce(lambda x,y: x + y, gen)
        prom = total/len(feno_final)
        return prom
    else:
        raise errores.NotFound("No se puede sacar el promedio de esta caracteristica")

# feno_final[0]
# print(ascendencia(9))
# print(índice_de_tamaño(0))
# valor_característica('GTC', 'Hernán Valdivieso')
# print(min('GTC'))
# print(max('GTA'))
# print(prom('CTC'))
#print(pariente_de(1, id_getter('Tomas Salvadores')))

