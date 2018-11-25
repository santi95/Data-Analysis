import datos
import collections

feno = datos.personas_genotipo
geno = datos.personas
#ME ESTÄ SALIENDO DE A POCOOO!

def color_ojos(id_persona):
    genes = feno[id_persona].diccionario_genes['GTC']
    if 'CCT' in genes:
        return 'Cafés'
    elif 'AAT' in genes and 'CCT' not in genes:
        return 'Azules'
    else:
        return 'Verdes'

def color_pelo(id_persona):
    genes = feno[id_persona].diccionario_genes['GGA']
    if 'GTG' in genes:
        return 'Negro'
    elif 'AAT' in genes and 'GTG' not in genes:
        return 'Rubio'
    else:
        return 'Pelirrojo'

def nariz(id_persona):
    genes = feno[id_persona].diccionario_genes['GTA']
    if 'TCG' in genes:
        return 'Aguileña'
    elif 'CAG' in genes and 'TCG' not in genes:
        return 'Respingada'
    else:
        return 'Recta'

def tono(id_persona):
    genes = feno[id_persona].diccionario_genes['TCT']
    counter = collections.Counter(genes)
    blanco = counter['AAT'] ; oscuro = counter['GCG']
    total = blanco + oscuro
    propo = blanco/total
    # if blanco/oscuro == 1/2:
    #     return 'Morenazo'
    if propo >= 0.75:
        return 'Albino'
    elif propo >= 0.5:
        return 'Blanco'
    elif propo >=  0.25:
        return 'Moreno'
    elif propo >= 0:
        return 'Negro'

def guata(id_persona):
    genes = feno[id_persona].diccionario_genes['TGG']
    counter = collections.Counter(genes)
    grande = counter['AGT'] ; chica = counter['ACT']
    total = grande + chica
    propo = chica/total
    if propo >= 0.75:
        return ('Modelo', 0)
    elif propo >= 0.5:
        return ('Atleta', 1)
    elif propo >=  0.25:
        return ('Mañana empiezo la dieta', 2)
    elif propo >= 0:
        return ('Guatón Parrillero', 3)


def altura(id_persona):
    genes = feno[id_persona].diccionario_genes['AAG']
    counter = collections.Counter(genes)
    alto = counter['ACT'] ; bajo = counter['AGT']
    total = alto + bajo
    propo = alto/total
    if alto/total == 0.75:
        return 1.925
    else:
        #return round(1.4 + 0.7*propo, 2)
        return (1.4 + 0.7*propo)

def pies(id_persona):
    genes = feno[id_persona].diccionario_genes['CTC']
    counter = collections.Counter(genes)
    grandes = counter['GTA'] ; chicos = counter['CCA']
    total = grandes + chicos
    propo = grandes/total
    return round(34 + 14*propo)

def vello(id_persona):
    genes = feno[id_persona].diccionario_genes['CGA']
    counter = collections.Counter(genes)
    axila = counter['GTG'] ; espalda = counter['CCT']; pecho = counter['TGC']
    total = axila + pecho + espalda
    if total == 0: return []
    axila1 = axila/total ; pecho1 = pecho/total ; espalda1 = espalda/total
    lista_vello = []
    if axila1 > 0.2:
        lista_vello.append('Axila')
    if pecho1 > 0.2:
        lista_vello.append('Pecho')
    if espalda1 > 0.2:
        lista_vello.append('Espalda')
    return lista_vello

def vision(id_persona):
    genes = feno[id_persona].diccionario_genes['TAG']
    counter = collections.Counter(genes)
    dalto = counter['TTC'] ; miopia = counter['ATT']
    total = dalto + miopia
    if total == 0: return []
    dalto1 = dalto/total ; miopia1 = miopia/total
    lista_vision = []
    if dalto1 > 0.2:
        lista_vision.append('Daltonismo')
    if miopia1 > 0.2:
        lista_vision.append('Miopía')
    return lista_vision

def crear_fenotipo(i):
    altura2 = altura(i)
    color_ojos2 = color_ojos(i)
    color_pelo2 = color_pelo(i)
    tono2 = tono(i)
    nariz2 = nariz(i)
    pies2 = pies(i)
    guata2 = guata(i)
    vello2 = vello(i)
    vision2 = vision(i)
    feno_final.append(persona(i, feno[i].nombre,
                               feno[i].apellido,
                               altura2, color_ojos2,
                               color_pelo2, tono2,
                               nariz2, pies2,
                               guata2, vello2,
                               vision2))
    if i < len(feno) - 1:
        crear_fenotipo(i+1)

persona = collections.namedtuple('Persona', 'id, '
                                            'nombre, '
                                            'apellido, '
                                            'altura, '
                                            'color_ojos, '
                                            'color_pelo, '
                                            'tono, nariz, '
                                            'pies, guata,'
                                            ' vello, vision')
feno_final = []
crear_fenotipo(0)

# for i in range(len(feno_final)):
#     print(feno_final[i])




